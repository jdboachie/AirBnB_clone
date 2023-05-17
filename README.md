# AirBnB clone - The console

## Description

The AirBnB clone project is a part of the Holberton School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management.

The command interpreter allows users to create, retrieve, update, and delete objects in a database. The objects that can be managed are:

* Users
* Places
* Reviews

### How to start it

To start the command interpreter, run the following command in your terminal:

``` shell
./console
```

### How to use it

The command interpreter is a Python program that uses the Click library to define its commands. To see a list of all available commands, run the following command:

``` shell
./console --help
```

To get help on a specific command, run the following command:

``` shell
./console help <command>
```

For example, to get help on the `create_user` command, run the following command:

``` shell
./console help create_user
```

### Examples

Here are some examples of how to use the command interpreter:

* To create a new user, run the following command:

``` shell
./console create_user <username> <email> <password>
```

* To retrieve a user by their username, run the following command:

``` shell
./console get_user <username>
```

* To update a user's email address, run the following command:

``` shell
./console update_user <username> <email>
```

* To delete a user, run the following command:

``` shell
./console delete_user <username>
```

### AUTHORS

The authors of this project are:

* Beatrice Addison Winful [@ttrice197](https://github.com/ttrice197)
* Jude Boachie [@jdboachie](https://github.com/jdboachie)

### Branches and pull requests

This project uses branches and pull requests to organize work. To create a new branch, run the following command:

``` shell
git checkout -b <branch_name>
```

To merge a branch into the master branch, run the following command:

``` shell
git merge <branch_name>
```

To push changes to the remote repository, run the following command:

``` shell
git push
```

To pull changes from the remote repository, run the following command:

``` shell
git pull
```

I hope this helps!
