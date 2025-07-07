import tweepy
import os

# Load Twitter credentials from environment variables
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Read tips from file
with open("tips.txt", "r", encoding="utf-8") as f:
    tips = [line.strip() for line in f if line.strip()]

# Read last posted index
index_file = "last_tip_index.txt"
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        last_index = int(f.read().strip())
else:
    last_index = -1  # no tip posted yet

# Get next tip in sequence
next_index = (last_index + 1) % len(tips)  # loops back to start if done
tip = tips[next_index]

# Create tweet text
tweet = f"💡 Daily Coding Tip #{next_index + 1}\n\n{tip}\n\n#100DaysOfCode #CodingTips #DevTips"

print("👉 Copy and post this tweet manually:\n")
print(tweet)
print(f"📌 This was Tip #{next_index + 1}")


# Update index for next run
with open(index_file, "w") as f:
    f.write(str(next_index))
