package fetch

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
	"sync"
	"time"
)

type Fetch struct {
	baseUrl string
	// channel receiving success data from API
	successData chan struct {
		Name string
		Data []byte
	}
	// channel receiving error from API request
	errData chan struct {
		Name  string
		Error string
	}
	// As signal for the sender to successData/errData when
	// worker has done processing data
	done chan struct{}
}

func New(baseUrl string) *Fetch {
	fetch := &Fetch{
		baseUrl: baseUrl,
		successData: make(chan struct {
			Name string
			Data []byte
		}),
		errData: make(chan struct {
			Name  string
			Error string
		}),
		done: make(chan struct{}),
	}

	// Call a function that will call goroutine
	// listening to channel successData and errData
	fetch.Listen()
	return fetch
}

func (fetch *Fetch) Listen() {
	go func() {
		for {
			select {
			// if a success data is received, then this block
			// is executed and signal fetch.done when it's done processing
			case data := <-fetch.successData:
				fetch.Display(data)
				fetch.done <- struct{}{}
			// if a error data is received, then this block
			// is executed and signal fetch.done when it's done processing
			case data := <-fetch.errData:
				fetch.Display(data)
				fetch.done <- struct{}{}
			}

		}
	}()
}

// Just a normal HTTP Request
func (fetch *Fetch) Request(url string, method string, body io.Reader) ([]byte, error) {
	callCtx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	req, err := http.NewRequestWithContext(callCtx, method, url, body)
	if err != nil {
		return nil, err
	}

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, err
	}

	resBody, err := io.ReadAll(res.Body)
	defer res.Body.Close()
	if err != nil {
		return nil, err
	}

	return resBody, nil
}

// GetCovidStatsCountry is a wrapper around fetch.Request with endpoints vary by countries
// It will fetch Covid-19 stats by country given
func (fetch *Fetch) GetCovidStatsByCountry(country string) ([]byte, error) {
	endpoint := url.QueryEscape(strings.ToLower(country))
	countryUrl := fmt.Sprintf("%s/%s", fetch.baseUrl, endpoint)
	return fetch.Request(countryUrl, "GET", nil)
}

// GetCovidStats is a more generic wrapper around fetch.Request.
// The idea is, it will fetch multiple countries concurrently.
func (fetch *Fetch) GetCovidStats() {
	countries := []string{
		"malaysia",
		"indonesia",
		"thailand",
		"vietnam",
		"brunei",
	}

	var wg sync.WaitGroup

	for _, c := range countries {
		wg.Add(1)
		go func(c string) {
			defer wg.Done()
			defer func() {
				if r := recover(); r != nil {
					fetch.errData <- struct {
						Name  string
						Error string
					}{
						Name:  c,
						Error: "Recovered from panic",
					}
					<-fetch.done
					return
				}
			}()
			by, err := fetch.GetCovidStatsByCountry(c)
			if err != nil {
				fetch.errData <- struct {
					Name  string
					Error string
				}{
					Name:  c,
					Error: err.Error(),
				}
				<-fetch.done
				return
			}

			fetch.successData <- struct {
				Name string
				Data []byte
			}{
				Name: c,
				Data: by,
			}
			<-fetch.done
		}(c)
	}

	wg.Wait()

}

// To show the data to stdout
func (fetch *Fetch) Display(data interface{}) {
	switch v := data.(type) {
	// If type is struct of success data,
	// then execute the block below
	case struct {
		Name string
		Data []byte
	}:
		fmt.Println("New data!")
		fmt.Println(string(v.Data))
	// If type is struct of error data,
	// then execute the block below
	case struct {
		Name  string
		Error string
	}:
		fmt.Println("New error!!!")
		fmt.Println(v.Error)
	// Safe guard when unexpected data is passed through this method
	default:
		fmt.Println("Unknown data")
	}

}
