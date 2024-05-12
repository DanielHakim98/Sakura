/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"
	"os"

	"github.com/DanielHakim98/worker-pool/worker"
	"github.com/spf13/cobra"
)

var (
	numTasks, numWorkers, numConsumers int
	url                                string
)

// workerCmd represents the worker command
var workerCmd = &cobra.Command{
	Use:   "worker",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		if numTasks < 0 {
			fmt.Fprintln(os.Stderr, "Error: argument 'task' value cannot be negative")
			fmt.Fprintln(os.Stderr, cmd.Usage())
			os.Exit(1)
		}

		if numWorkers < 0 {
			fmt.Fprintln(os.Stderr, "Error: argument 'worker' value cannot be negative")
			fmt.Fprintln(os.Stderr, cmd.Usage())
			os.Exit(1)
		}

		if numConsumers < 0 {
			fmt.Fprintln(os.Stderr, "Error: argument 'consumer' value cannot be negative")
			fmt.Fprintln(os.Stderr, cmd.Usage())
			os.Exit(1)
		}

		if url == "" {
			fmt.Fprintln(os.Stderr, "Error: invalid argument 'url'")
			fmt.Fprintln(os.Stderr, cmd.Usage())
			os.Exit(1)
		}

		worker.Run(numTasks, numWorkers, numConsumers, url)
	},
}

func init() {
	rootCmd.AddCommand(workerCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// workerCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// workerCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
	workerCmd.Flags().IntVarP(&numWorkers, "worker", "w", 1, "number of workers. default is 1")
	workerCmd.Flags().IntVarP(&numTasks, "task", "t", 1, "number of tasks. default is 1")
	workerCmd.Flags().IntVarP(&numConsumers, "consumer", "c", 1, "number of consumer, default is 1")

	workerCmd.Flags().StringVarP(&url, "url", "u", "", "url link to be tested")
}
