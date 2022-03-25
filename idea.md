{% include navigation.html %}

hook, overview, link or embed to deployment

Deployment with AWS Coming Soon!
# Our website hosting plan
### Our website will be run on Amazon Web Services. What is detailed below is the plan for hosting.

1. Choose an Amazon Machine Image (AMI)Cancel and Exit
    - Ubuntu Server 20.04
2. Choose Instance Type
3. Launch and assign a key pair
4. Setup Virtual environment and clone code from GitHub
    - *Activate virtual environment prior to updating packages
    - *Verify Python virual environment and package dependencies, if it fails pip install dependency
5. Test Python + Gunicorn run in browser
6. Build Gunicorn configuration file
7. Build Nginx configuration file
8. Validate Gunicorn configuration file and enable service permanently
9. Validate Nginx configuration file and enable service permanently
10. DNS, prepare Internet to route to Nginx server
    - Freenom -> register IP to domain, Port forward
11. Prepare Nginx configurations for HTTPS
    - Certbot
