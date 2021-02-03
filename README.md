# bunk-inator
A smart screen capture cli application

## bunk-inator in action 🎥

<img src="screenshots/bunkinatorScreenCapture.gif" alt="bunkinator screen capture">

### Requirements
- [Python](https://python.org)

### How to run
- download or `git clone` this repository
- `cd bunk-inator`
- `python -m pip install -r requirements.txt`
- `python main.py`

### How it works 
`bunk-inator` takes a screenshot of the selected capture area every `5` seconds by default
which can be changed by changing the value of global variable `frequency`, then it smartly compares
this screenshot with the one that was taken before this one and if there is a change in the new
screenshot it saves it otherwise discards it.

### limitations
- It has only been tested on windows, so it could cause some errors on linux or mac
- On a multiple monitor setup it'll only take screenshots of primary monitor
