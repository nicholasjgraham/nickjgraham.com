# NickJGraham.com

This repository hosts all of the code that is used to build and deploy my website, nickjgraham.com.

## Site Layout

### /

The home page, which should contain essentially a resume, along with some links to the other pages.

Should contain links to:

- /about
- Contact email
- Github
- Important technologies
- LinkedIn

### /about

A page that describes how the site is built and hosted. It actually contains way more information about how the site operates than this README does.

## Building

This website is primarily HTML5, with some Python to actually run the web services. Because of this, it's all interpreted and doesn't need to be 'built'.

However, it's also containerized, so a container image needs to be generated. The process for this is defined in `Jenkinsfile`, but is essentially:

``` docker build -t nicholasjgraham/nickjgraham.com:latest --build-arg BUILD_NUMBER=0 --build-arg BRANCH_NAME=manual . ```

## Deployment

The container image for this project can be deployed to any standard Docker environment. However, the live version of this site lives on a Kubernetes cluster. The definition for the Kubernetes environmment for this service can be found in `/deploy/nickjgrahamcom.yaml`

## Testing

This app was developed using Visual Studio Code, and because of that there is a launch configuration for local testing. This does not utilize Docker, so full build validation must be done through the CI system.

Note: In order to run this locally, you'll need to install [wkhtmltopdf](https://wkhtmltopdf.org/index.html).

## Special Thanks

Creation of this site would not be possible without [Xiaoying Riley](https://themes.3rdwavemedia.com/), [HarnishDesign](https://harnishdesign.net/), and their great HTML templates.
