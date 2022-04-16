# Slack Notifier
Post messages to Slack channels

## Installation
Requires Python 3.7.3 and above
>python3 -m pip install -r requirements.txt

## Usage
### Command-Line Usage
Send a simple text message:
>python3 slack_notifier.py C2JF0923Q "Hello world!"

Or send markdown instead using the `-m` option:
>python3 slack_notifier.py C2JF0923Q "This is <https://github.com/ctrl-escp/slackNotifier|Slack Notifier>" -m

You can always run `python3 slack_notifier.py -h`
```
usage: slack_notifier.py [-h] [-t TOKEN] [-m] cid msg

Slack Notifier

positional arguments:
  cid                   The target channel id
  msg                   The message to send

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Bearer token for slack. If not provided, extracted
                        from 'slackToken' environment variable
  -m, --markdown        Send the message as a markdown block
```

### Programmatically
Get the tweets:
```python
from slack_notifier import SlackNotifier
sn = SlackNotifier("your slack_token")
sn.post_message("the channel id", "msg")
sn.post_message("the channel id", "This is <https://github.com/ctrl-escp/slackNotifier|Slack Notifier>", True)
```
