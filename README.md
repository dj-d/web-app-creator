# Web App Creator

This script create a web application base on url

## Dependencies

- python3
- nohup
- google-chrome-stable
- Linux
- X11

## Usage

| Option          | Description                      | Required | Default                  |
| --------------- | -------------------------------- | -------- | ------------------------ |
| --url           | Url of the web application       | Yes      |                          |
| --name          | Name of the application          | Yes      |                          |
| --startup-class | Startup class of the application | Yes      |                          |
| --icon-path     | Path of the icon                 | Yes      |                          |
| --exec-path     |                                  | No       | /usr/bin/{startup_class} |
| --path          |                                  | No       | /usr/bin                 |
| --comment       |                                  | No       | WebApp                   |
| --type          |                                  | No       | Application              |
| --categories    |                                  | No       | Network;WebBrowser       |
| --custom-path   |                                  | No       | /opt/{startup_class}     |

Examples:

```bash
sudo python3 main.py \
    --url https://url.com/things \
    --name Application name \
    --startup-class class-name \
    --icon-path /path/to/icon.png
```

```bash
sudo python3 main.py \
    --url https://url.com/things \
    --name Application name \
    --startup-class class-name \
    --icon-path /path/to/icon.png \
    --custom-path /custom/application/path
```

## TODOs

- [ ] Check dependencies
- [ ] Add logging
- [ ] Add check on existing app
- [ ] Add check on existing icon
- [ ] Add check on existing custom path
- [ ] Add check on url
- [ ] Add check of icon extension
- [ ] Fix doc
