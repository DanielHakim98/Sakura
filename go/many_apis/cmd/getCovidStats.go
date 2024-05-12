/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"
	"log"
	"many-apis/pkg/config"
	"many-apis/pkg/fetch"

	"github.com/spf13/cobra"
)

// getCovidStatsCmd represents the getCovidStats command
var country string
var getCovidStatsCmd = &cobra.Command{
	Use:   "getCovidStats",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		config := config.GetConfig()
		fetcher := fetch.New(config.CovidUrl)
		by, err := fetcher.GetCovidStatsByCountry(country)
		if err != nil {
			log.Println(err)
		}

		fmt.Println(string(by))
	},
}

func init() {
	rootCmd.AddCommand(getCovidStatsCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// getCovidStatsCmd.PersistentFlags().String("foo", "", "A help for foo")
	getCovidStatsCmd.Flags().StringVarP(&country, "country", "c", "usa", "country name")
	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// getCovidStatsCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
