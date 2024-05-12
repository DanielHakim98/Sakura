/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"many-apis/pkg/config"
	"many-apis/pkg/fetch"

	"github.com/spf13/cobra"
)

// getCovidStatsTestCmd represents the getCovidStatsTest command
var getCovidStatsTestCmd = &cobra.Command{
	Use:   "getCovidStatsTest",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		config := config.GetConfig()
		fetcher := fetch.New(config.CovidUrl)
		fetcher.GetCovidStats()

	},
}

func init() {
	rootCmd.AddCommand(getCovidStatsTestCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// getCovidStatsTestCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// getCovidStatsTestCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
