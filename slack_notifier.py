import json
import requests


class SlackNotifier:
	chat_post_message_url = "https://slack.com/api/chat.postMessage"

	def __init__(self, token):
		self.headers = {
			"Content-Type": "application/json; charset=utf-8",
			"Authorization": f"Bearer {token}"
		}

	def post_message(self, channel_id, text):
		msg = {
			"channel": channel_id,
			"text": text
		}
		r = requests.post(self.chat_post_message_url, data=json.dumps(msg), headers=self.headers)
		if r.status_code != 200:
			print(json.dumps(r.json(), indent=2))


if __name__ == '__main__':
	import os
	from argparse import ArgumentParser

	parser = ArgumentParser(description="Slack Notifier")
	parser.add_argument("cid", action="store", type=str, help="The target channel id")
	parser.add_argument("msg", action="store", type=str, help="The message to send")
	parser.add_argument("-t", "--token", action="store", type=str,
						help="Bearer token for slack. If not provided, extracted from 'slackToken' environment variable")
	args = parser.parse_args()

	slack_token = args.token or os.environ.get("slackToken")
	if not slack_token:
		print("Error: No token provided. You must provide a slack token in order to post messages.")
	else:
		sn = SlackNotifier(slack_token)
		sn.post_message(args.cid, args.msg)
