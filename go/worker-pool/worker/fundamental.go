package worker

import (
	"fmt"
	"io"
	"net/http"
	"sync"
)

type Result struct {
	taskId, workerId int
	value            []byte
	err              error
}

func consumer( /*id int,*/ wg *sync.WaitGroup, results <-chan Result) {
	// fmt.Println("Consumer ID '", id, "' init")
	defer wg.Done()
	for res := range results {
		fmt.Println(string(res.value))
	}
}

func request(url string) ([]byte, error) {
	client := http.Client{}
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return []byte{}, err
	}

	resp, err := client.Do(req)
	if err != nil {
		return []byte{}, err
	}
	defer resp.Body.Close()

	by, err := io.ReadAll(resp.Body)
	if err != nil {
		return []byte{}, err
	}

	return by, nil
}

func worker(id int, wg *sync.WaitGroup, results chan<- Result, tasks <-chan Task) {
	// fmt.Println("Worker ID '", id, "' init")
	defer wg.Done()
	for task := range tasks {
		res, err := request(task.url)
		if err != nil {
			results <- Result{
				taskId:   task.id,
				workerId: id,
				err:      err,
			}
			continue
		}
		results <- Result{
			taskId:   task.id,
			workerId: id,
			value:    res,
		}
	}
}

type Task struct {
	id  int
	url string
}

func Run(numTasks, numWorkers, numConsumers int, url string) {

	results := make(chan Result, numWorkers)
	tasks := make(chan Task, numWorkers)

	wgConsumer := new(sync.WaitGroup)
	for cId := 1; cId <= numConsumers; cId++ {
		wgConsumer.Add(1)
		go consumer( /*cId,*/ wgConsumer, results)
	}

	wgWorker := new(sync.WaitGroup)
	for wId := 1; wId <= numWorkers; wId++ {
		wgWorker.Add(1)
		go worker(wId, wgWorker, results, tasks)
	}

	for tId := 1; tId <= numTasks; tId++ {
		tasks <- Task{
			id:  tId,
			url: url,
		}
	}

	close(tasks)
	wgWorker.Wait()
	close(results)
	wgConsumer.Wait()

}
