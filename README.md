# TechCafe Discord Bot

This repository contains the code for the TechCafe Discord bot, which provides various features to enhance the experience in the TechCafe Discord server.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The TechCafe Discord Bot is designed to assist and enhance interactions within the TechCafe Discord server. It provides commands and features that make it easier for members to engage and communicate effectively.

## Getting Started

To get started with the TechCafe Discord Bot, you'll need to follow these steps:

1. Clone the repository to your local machine.
2. Set up a Python environment with the required dependencies.
3. Configure your Discord bot token and other environment variables in the `.env` file.
4. Run the bot using Docker Compose or by executing the `runner.py` script.

## Features

- **Text Editing**: The bot includes a text editor module that allows users to send formatted announcements using slash commands.

- **Welcome Messages**: The bot greets new members who join the server with a welcome message in a designated channel.

- **Ping Command**: A simple ping command to check the bot's latency.

- **Customization**: The bot's features can be customized and extended through various modules.

## Usage

1. Install Docker and Docker Compose on your machine.

2. Create a `.env` file in the `envs/prod/discord` directory with the following content:

   ```
   BOT_TOKEN=YOUR_BOT_TOKEN
    ```

3. Build and run the bot using Docker Compose:
  ```
  docker-compose up --build
  ```
The bot should now be active on your Discord server.


## Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please feel free to open issues or submit pull requests.


## License
This project is licensed under the MIT License.
