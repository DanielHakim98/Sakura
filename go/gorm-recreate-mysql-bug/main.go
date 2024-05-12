package main

import (
	"context"
	"fmt"
	"time"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"gorm.io/gorm/clause"
)

type User struct {
	ID        uint64
	Email     string `gorm:"uniqueIndex:idx_email;type:varchar(256);"`
	UpdatedAt time.Time
	CreatedAt time.Time
}

type UserDB struct {
	db *gorm.DB
}

func (u *UserDB) Create(ctx context.Context, models []*User) error {
	return u.db.WithContext(ctx).Clauses(clause.OnConflict{
		Columns:   []clause.Column{{Name: "email"}},
		DoUpdates: clause.AssignmentColumns([]string{"updated_at"}),
	}).CreateInBatches(models, 1).Error
}

func main() {
	dsn := "user:password@tcp(127.0.0.1:3306)/db?charset=utf8mb4&parseTime=True&loc=Local"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("could not initialize db")
	}

	user := UserDB{db}
	user1 := &User{Email: "test@test.com"}
	user2 := &User{Email: "apple@apple.com"}
	createErr := user.Create(context.TODO(), []*User{
		user1, user2,
	})
	if createErr != nil {
		panic("err: " + createErr.Error())
	}
	fmt.Println("Created successfully")
	fmt.Println("user1 id:", user1.ID)
	fmt.Println("user2 id:", user2.ID)
}
