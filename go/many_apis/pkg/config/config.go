package config

import (
	"log"

	"github.com/spf13/viper"
)

type Config struct {
	CovidUrl string `mapstructure:"COVID_COUNTRY_URL"`
}

func GetConfig() *Config {
	viper.AddConfigPath(".")
	viper.SetConfigName("app")
	viper.SetConfigType("env")
	viper.AutomaticEnv()

	err := viper.ReadInConfig()
	if err != nil {
		log.Fatal(err)
	}

	var config Config
	err = viper.Unmarshal(&config)
	if err != nil {
		log.Fatal(err)
	}

	return &config
}
