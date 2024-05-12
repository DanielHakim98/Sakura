package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"time"

	"context"
)

func main() {
	handlers := NewHandlers(4, 5)
	http.HandleFunc("/poc/", handlers.Middleware(handlers.Get))
	fmt.Println("Server starting & listening at 8080")
	fmt.Println()
	http.ListenAndServe(":8080", nil)
}

func NewHandlers(worker, timeout int) *Handlers {
	h := Handlers{
		worker:  worker,
		timeout: timeout,
		pipe:    make(chan interface{}),
	}
	return &h
}

type Handlers struct {
	worker  int
	timeout int
	pipe    chan interface{}
}

type Response struct {
	Status  int         `json:"status"`
	Message string      `json:"message"`
	Data    interface{} `json:"data"`
}

type UserSettings string

func (h *Handlers) Middleware(
	handler func(http.ResponseWriter, *http.Request)) func(http.ResponseWriter, *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		urlParams := r.URL.Query()
		workerParam := urlParams.Get("worker")
		timeoutParam := urlParams.Get("timeout")

		settings := HandlerSetting{
			worker:  h.worker,
			timeout: h.timeout,
		}
		defer func() {
			fmt.Printf("reset -> worker: %v, timeout: %v\n", h.worker, h.timeout)
		}()
		if workerParam != "" {
			newWorker, err := strconv.Atoi(workerParam)
			if err != nil {
				w.WriteHeader(http.StatusBadRequest)
				json.NewEncoder(w).Encode(Response{
					Status:  http.StatusBadRequest,
					Message: "worker not a number",
					Data:    nil,
				})
				return
			}
			settings.worker = newWorker
		}

		if timeoutParam != "" {
			newTimeout, err := strconv.Atoi(timeoutParam)
			if err != nil {
				w.WriteHeader(http.StatusBadRequest)
				json.NewEncoder(w).Encode(Response{
					Status:  http.StatusBadRequest,
					Message: "timeout not a number",
					Data:    nil,
				})
				return
			}
			settings.timeout = newTimeout
		}
		fmt.Println(settings)
		ctx := context.WithValue(r.Context(), UserSettings("user"), settings)
		r = r.WithContext(ctx)
		start := time.Now()
		handler(w, r)
		fmt.Printf("executed -> worker: %v, timeout: %v, time taken: %v\n", settings.worker, settings.timeout, time.Since(start))

	}

}

type HandlerSetting struct {
	worker  int
	timeout int
}

func (h *Handlers) Get(w http.ResponseWriter, r *http.Request) {
	// w.Header().Set("Content-Type", " application/json")
	val := r.Context().Value(UserSettings("user"))
	settings, ok := val.(HandlerSetting)
	if !ok {
		w.WriteHeader(http.StatusInternalServerError)
		json.NewEncoder(w).Encode(Response{
			Status:  500,
			Message: "could not retrieve context for this request",
			Data:    nil,
		})
		return
	}

	msg := h.process(settings.timeout)
	json.NewEncoder(w).Encode(Response{
		Status:  200,
		Message: "OK",
		Data:    msg,
	})
}

func (h *Handlers) process(randNum int) (data string) {
	// randNum := rand.Intn(6-1) + 1
	data = fmt.Sprintf("Sleep for %v second(s)", randNum)
	fmt.Println(data)
	time.Sleep(time.Duration(randNum) * time.Second)
	return
}
