# Cash on Cash Calculator
Repo for IDS721 Cloud Project 2: Docker Container Project

The purpose of this project is to use Docker containers to deploy a simple Python program, push the image to DockerHub, then pull the image down and run it on a cloud platform cloud shell. Here, I've built a simple cash on cash calculator based on purchasing price, HOA fees, property tax, and home insurance. This can help identify properties that are more likely to be a better investment. 

## Usage

1. Pull the image from DockerHub: `docker pull vmtang11/docker_project:latest`
2. Run it: `docker run -it vmtang11/docker_project python app.py --pp 415000 --hoa 885 --tax 740 --ins 145 --rent 3000`. Here, you can pass in any values for purchasing price in addition to monthly HOA, property tax, home insurance, and rent.

Example Output: <br>
`Your estimated cash on cash is 3.56%.`
