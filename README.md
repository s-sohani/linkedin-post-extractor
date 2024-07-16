# LinkedIn Post Extractor
This project helps you to extract LinkedIn posts and save them as images or text files. It is useful for archiving, sharing, or analyzing your LinkedIn content. The extractor uses a combination of web scraping and automation tools to navigate LinkedIn, capture posts, and save them in the desired format.

## Features
- **Extract Posts as Images:** Capture the visual appearance of your LinkedIn posts.\
- **Extract Posts as Text:** Save the textual content of your LinkedIn posts.\
- **Automated Browsing:** Uses Google Chrome and ChromeDriver to automate the browsing process.\
- **Easy to Use:** Simple command-line interface to start the extraction process.\

## Installation
To get started with the LinkedIn Post Extractor, follow these installation steps:

### Install Google Chrome:

```bash
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install -y google-chrome-stable
```

### Install ChromeDriver:

```bash
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```
### Install Python Dependencies:
```bash
pip3 install -r requirements.txt
```

## Usage
To use the LinkedIn Post Extractor, follow these steps:

1. **Prepare LinkedIn Credentials:** Ensure you have your LinkedIn login credentials ready. The extractor will need these to log in and access your posts.

2. **Run the post-extractor:**

```bash 
python3 post-extractor.py
```
>The script will prompt you to enter your LinkedIn credentials and then proceed to extract your posts.

3. **Choose Output Path:** Select whether you want to save the posts as images or text files.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

## License
This project has no any License. 

## Acknowledgments
- Thanks to the developers of Selenium for providing the tools necessary to automate web browsing.
- Inspired by the need to archive and analyze professional social media content.
## Contact
For any questions or support, please contact [m.s.sohani73@gmail.com](m.s.sohani73@gmail.com).

