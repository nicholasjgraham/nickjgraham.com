# This file contains variables that are used to populate different areas of the resume that is generated.
# It's a little overkill and unnecessary, considering that editing HTML is just as easy, but it's also more fun to implement this way.

from flask import url_for

# Define link_list, which will be a list of keywords that are automatically hyperlinked on the resume page

link_list = {
    "Ansible": "https://www.ansible.com/",
    "Mulesoft": "https://www.mulesoft.com/",
    "Tomcat": "https://tomcat.apache.org/",
    "Kubernetes": "https://kubernetes.io/",
    "Jenkins": "https://www.jenkins.io/",
    "Xerox": "https://www.xerox.com/",
    "VMware": "https://www.vmware.com/",
    "Commvault": "https://www.commvault.com/",
    "Single Sign-On": "https://www.pingidentity.com/en/pingone/pingfederate.html",
    "VMware Orchestrator": "https://www.vmware.com/products/vrealize-orchestrator.html",
    "Microsoft Deployment Toolkit": "https://learn.microsoft.com/en-us/mem/configmgr/mdt/",
    "Spiceworks": "https://www.spiceworks.com/free-help-desk-software/self-hosted/",
    "CI/CD": "https://www.redhat.com/en/topics/devops/what-is-ci-cd",
    "Python": "https://www.python.org/",
    "Git": "https://git-scm.com/",
    "AWS": "https://aws.amazon.com/",
}

# Define the "Resume" class, which will include all of the different components we want to inject into the HTML template


class Resume:
    def __init__(self, name, title):
        # Define all of the attributes we want to keep track of with this class.
        # Initially, we just set everything to placeholder values, and we'll create and use set methods to update those values later
        self.name = name
        self.title = title
        self.email = f"{name}&commat;example&period;com"
        self.linkedin = 'https://linkedin.com'
        self.github = 'https://github.com'
        self.website = 'https://example.com'
        self.summary = 'This is a summary of your career experience.'
        self.work_experience = [
            {
                'title': 'First Job Title',
                'company': 'First Company',
                'date': '2020 - Present',
                'description': 'This is a lengthy description of your time at First Company.',
                'achievements': [
                    'This is a compelling list of your achievements at First Company.',
                    'You should include multiple of them.',
                    'Unless you only did one thing.',
                    'But that would be strange.'
                ],
                'technologies': {
                    'These',
                    'Are',
                    'The',
                    'Technologies',
                    'You',
                    'Use'
                }
            },
            {
                'title': 'Second Job Title',
                'company': 'Second Company',
                'date': '2016 - 2020',
                'description': 'This is a lengthy description of your time at Second Company.',
                'achievements': [
                    'This is a compelling list of your achievements at Second Company.',
                    'You should include multiple of them.',
                    'Unless you only did one thing.',
                    'But that would still be strange.'
                ],
                'technologies': {
                    'These',
                    'Are',
                    'The',
                    'Technologies',
                    'You',
                    'Also',
                    'Used'
                }
            }
        ]
        self.main_skills = {
            'Skill Category 1': {
                'Skill 1',
                'Skill 2',
                'Skill 3'
            },
            'Skill Category 2': {
                'Skill 1',
                'Skill 2',
                'Skill 3'
            }
        }
        self.other_skills = {
            'Other Skill 1',
            'Other Skill 2',
            'Other Skill 3',
            'Other Skill 4'
        }
        self.education = [
            {
                'degree': 'Latest Degree Name',
                'name': 'University Name',
                'date': '2018'
            },
            {
                'degree': 'Earliest Degree Name',
                'name': 'University Name',
                'date': '2014'
            }
        ]
        self.certs = [
            {
                'name': 'CERTA',
                'date': 'current',
                'url': 'https://google.com'
            },
            {
                'name': 'CERTB',
                'date': '2015'
            }
        ]
        self.interests = {
            'Interest 1',
            'Interest 2'
        }

    def set_email(self, email):
        self.email = email

    def set_linkedin(self, linkedin):
        self.linkedin = linkedin

    def set_github(self, github):
        self.github = github

    def set_website(self, website):
        self.website = website

    def set_summary(self, summary):
        self.summary = summary

    def set_work_experience(self, work_experience):
        self.work_experience = work_experience

    def set_main_skills(self, main_skills):
        self.main_skills = main_skills

    def set_other_skills(self, other_skills):
        self.other_skills = other_skills

    def set_education(self, education):
        self.education = education

    def set_certs(self, certs):
        self.certs = certs

    def set_interests(self, interests):
        self.interests = interests


def get_resume():
    # Create a default resume object
    resume = Resume('Nick Graham', 'Principal Infrastructure Engineer')

    # Customize

    resume.set_email('nick&commat;nickjgraham&period;com')

    resume.set_linkedin('https://www.linkedin.com/in/ngraham2/')

    resume.set_github('https://github.com/nicholasjgraham')

    resume.set_website('https://nickjgraham.com')

    resume.set_summary('''I'm Nick, an experienced systems engineer with a wide range of proficiencies ranging from simple Linux administration to complex automated application service deployments with Kubernetes.

    Over the years I've worked to develop a broad set of skills across the IT space, and at the moment I'm using those to support developers and projects at <a href="https://www.cdphp.com/">Capital District Physician\'s Health Plan</a>, a regional health insurance company in upstate New York.
    ''')

    resume.set_work_experience([
        {
            'title': 'Principal Infrastructure Engineer',
            'company': 'Capital District Physician\'s Health Plan',
            'date': '2016 - Present',
            'description': '''As a leader on the Linux engineering team I serve as the subject matter expert for Linux and its related technology stack. My responsibilities include creating architecture solutions, overseeing technology projects to completion, and implementing automation processes that reduce toil and solve business problems. I provide leadership in decision-making and hold responsibility for my team members.

            In addition to these duties, I manage monitoring and incident response, ensuring high availability and system uptime. I also act as a liaison between the development and infrastructure teams, facilitating seamless collaboration and ensuring that developers have the tools and support they need to efficiently write and deploy code.

            I primarily operate in a Linux environment on AWS and VMware, utilizing tools such as Kubernetes, Git, Ansible, Jenkins, and Python to build and maintain application server systems and pipelines that serve developers and business units.
            ''',
            'achievements': [
                'Architected and executed Single Sign-On (SSO) system expansion to AWS, creating a multi-region, highly available system with no downtime since its creation. This greatly improved the reliability of our authentication system for both employees and customers.',
                'Fully automated deployment and configuration management of Mulesoft application server architecture using Ansible, including over 80 individual services across 4 SDLC environments. This allowed for consistent, reliable, quick deployments of new services and updates.',
                'Led the containerization of legacy Tomcat services into fully automated, reliable solution on Kubernetes. This enabled developers to deploy new services with minimal effort, and provided a consistent, reliable platform for those services to run on.',
                'Created many CI/CD pipelines in Jenkins to turn complex processes like code builds, file deployments, or configuration changes into scheduled, or one-click operations. This greatly reduced the time and effort required to deploy changes, as well as reducing the chance for human error.',
                'Automated the transition from CentOS to RHEL, and subsequent upgrades to RHEL 9. This reduced the amount of labor required to perform these upgrades by the whole engineering staff.',
                'Organized and streamlined Ansible playbook usage, including the development of easy-to-use environment build scripts, and personal training/mentoring for other engineers. This enhanced the use of Ansible and improved automation capabilities for everyone\'s work across the team.',
                'Created a custom internal site with Python that integrates with our SSO system APIs. This provides users across the company with a central place to find SSO links, rather than relying on links maintained in wikis or emails.'
            ],
            'technologies': {
                'Ansible',
                'Jenkins',
                'Kubernetes',
                'Linux',
                'Mulesoft',
                'Nginx',
                'OpenTelemetry',
                'Packer',
                'Ping Federate',
                'Python',
                'Red Hat Enterprise Linux',
                'Sumologic',
                'Terraform',
                'Tomcat',
                'Windows'
            }
        },
        {
            'title': 'Systems Engineer',
            'company': 'Xerox Corporation',
            'date': '2013 - 2016',
            'description': 'At Xerox I quickly rose to become the subject matter expert for a number of systems including our VMware infrastructure (thousands of hosts across 6 datacenters in the US, UK, and China), Commvault backup infrastructure, as well as an automated self-service tool I created that employees used to build sandbox environments and adjust the scale of production services. I also acted as a general systems engineering resource for both Windows and Linux server work.',
            'achievements': {
                'Architected and implemented up all of the backup infrastructure required to support disaster recovery for all of Xerox\'s systems',
                'Led VMware expansion to two new datacenters in China, including hardware purchasing, deployment, and configuration.',
                'Created a VM deployment process automation from the ground up with VMware Orchestrator.',
                'Enhanced the system lifecycle process around all of our VMware infrastructure. Everything from creation of new servers, patching existing ones, updating configurations, and server decommissioning was streamlined and automated in some way.'
            },
            'technologies': {
                'Commvault Simpana',
                'Linux',
                'Powershell',
                'SUSE Linux Enterprise Server',
                'VMware',
                'Windows Server'
            }
        },
        {
            'title': 'Information Systems Intern',
            'company': 'Saratoga Hospital',
            'date': '2013 - 2013',
            'description': 'For my senior year of college, right before graduating, I took up an internship with one of the larger hospitals close to me. There I learned about the interpersonal nature of IT, helping users and developers get what they need, more than I ever had in any of my college classes. I also started delving into automation and found my love for reducing toil.',
            'achievements': {
                'Created a fully featured PC deployment solution using the Microsoft Deployment Toolkit (MDT). Before my arrival PC deployments were all done manually, clicking through the installer. After deploying MDT new PC builds were as simple as starting a machine and selecting the PXE boot option.',
                'Created custom code for the ticket tracking system (Spiceworks), in order to add some custom fields and workflows that the base product didn\'t provide.'
            },
            'technologies': {
                'Javascript',
                'Microsoft Deployment Toolkit',
                'Windows Server'
            }
        },
        {
            'title': 'IT Technician',
            'company': 'SUNY Canton',
            'date': '2009 - 2013',
            'description': 'While in college I worked in my school\'s IT department. There I worked alongside the more senior networking staff and acted as a junior network engineer; making smaller scale cabling changes, adjusting VLANs and port statuses on switches, and just generally helping out around the shop.',
            'achievements': {
                'Created a PHP application called <a href="https://sourceforge.net/projects/netinv/">NETINV</a> to track the association between switches, patch panel ports, and wall ports in classrooms. Identifying where various switch ports went was a huge hassle at the time, and my contribution removed the painful process of having to manually trace out each network connection when making port changes.'
            },
            'technologies': {
                'Linux',
                'Networking',
                'PHP'
            }
        }
    ])

    resume.set_main_skills({
        'Professional': {
            'Effective Communication',
            'Problem Solving',
            'Project Management',
            'Teamwork'
        },
        'Technical': {
            'Ansible',
            'Apache HTTPd',
            'Appdynamics',
            'Artifact Repositories',
            'Bash',
            'Commvault Simpana',
            'Docker',
            'HashiCorp Packer',
            'HashiCorp Terraform',
            'Javascript',
            'Jenkins',
            'Kubernetes',
            'Linux',
            'Nginx',
            'Ping Federate (SAML/Oauth)',
            'Powershell',
            'Python',
            'VMware',
            'Windows Server'
        }
    })

    resume.set_other_skills({
        'Active Directory',
        'Amazon Web Services',
        'Artificial Intelligence (AI)',
        'Change Management',
        'Configuration Management',
        'Databases (MSSQL, MySQL)',
        'DNS',
        'Documentation',
        'ELK (Elasticsearch, Logstash, Kibana)',
        'IIS',
        'Large Language Models (LLMs)',
        'Log Management',
        'Mulesoft',
        'Nagios',
        'Networking',
        'Nginx',
        'Oauth',
        'Physical Server Administration (Blade/Rack)',
        'Rancher',
        'Red Hat Enterprise Linux (RHEL)',
        'SAN Management',
        'Sonatype Nexus',
        'Source Control (Git)',
        'SSL/TLS Certificates & Ciphers',
        'Sumologic',
        'System Integration',
        'Ubuntu',
        'VMware Horizon',
        'VMware PowerCLI'

    })

    resume.set_education([
        {
            'degree': 'Bachelor\'s, Information Technology',
            'name': 'SUNY Canton',
            'date': '2013'
        }
    ])

    resume.set_certs([
        {
            'name': 'VMware VCP6-DCV',
            'date': 'current',
            'url': url_for('static', filename='vcp6.pdf')
        },
        {
            'name': 'Cisco CCNA',
            'date': '2013'
        }
    ])

    resume.set_interests({
        '3D Printing',
        'Cars',
        'Landscaping',
        'Mechanics',
        'Music',
        'Robotics',
        'Volunteer Firefighter'
    })

    # Return the customized resume object
    return resume
