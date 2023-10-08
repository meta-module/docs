![https://logo.metamodule.org/1/cover.png](https://logo.metamodule.org/1/cover.png)

# MetaModule Documentation [docs.metamodule.org](http://docs.metamodule.org)

During writing a book on hypermodularisation, I had to create a specification of metamodules, which are a
specification of something that can be defined, i.e. a process, a service, a software, a role in a team....
it's such a digital representation of the definition of a module model.
Once we define the organisation as a network of metamodules, then we have a digital representation, a so-called digital twin: the digital twin

[Cyfrowy bliźniak – 3 przykłady użycia w logistyce - Mecalux.pl](https://www.mecalux.pl/blog/cyfrowy-blizniak-przyklady)

The benefits of simulating an organisation in the event of various scenarios, allows the consequences of the current organisation and infrastructure configuration to be anticipated, which provides the opportunity to increase service quality.

## TODO:

+ generation of connection graphs
+ creation of module map
+ linking other existing modules via generator (root)
+ creating a SQL query on the whole disk/user github
+ 

## graphQL

+ [https://cloud.dgraph.io](https://cloud.dgraph.io)

+ [https://nameless-brook-400255.eu-central-1.aws.cloud.dgraph.io/graphql](https://nameless-brook-400255.eu-central-1.aws.cloud.dgraph.io/graphql)


```
website:linkedin -> data:json -> informacje:contact
```

```
information:contact -> data:html -> website:footer
```

## install requirements:

The requirements can be loaded into the shell by using the pip command.
For example, to install the requirements listed in the requirements.txt file, run the following command:

```bash
pip install -r requirements.txt
chmod +x validation.py
```

## Start Example

```bash
py validation.py
```


## How it works ?

Example metamodule in json format with schema definition, schema validation, and dependencies with inharitences as url.

file: [metamodule/environment.json](metamodule/environment.json)
```json
{
  "validator": [
    "https://requirements.metamodule.org/1.0.1",
    "https://definition.metamodule.org/1.0.1",
    "https://lifecycle.metamodule.org/1.0.1"
  ],

  "generator": {
    "implementation": "https://imeplementation.metamodule.org/1.0.1",
    "test": "https://environment.metamodule.org/1.0.1",
    "lifecycle": "https://environment-lifecycle.metamodule.org/1.0.1"
  },

  "definition": {
    "name": "Environment for running tensorflow python application",

    "problem": "generate data to excel report about all invoices in selected folder",
    "solution": "convert PDF file to json data over script based on tensorflow",

    "type": "api",
    "version": "1.0.0",
    "author": "",
    "license": "",
    "website": "environment.metamodules.org",
    "git": "https://github.com/meta-modules/ocr-pdf.git"
  },

  "lifecycle": {
    "packages": {
      "nodejs": "17",
      "mariadb": "5",
      "docker": "https://hub.docker.com/r/andrewmackrodt/nodejs"
    },
    "config": {
      "username": "test",
      "path": "/home/test",
      "data": "storage",
      "settings": ".config"
    },
    "monitoring": {
      "latency": "1ms",
      "availability": "90%"
    }
  }
}

```


This JSON file describes the environment for running a tensorflow python application.
It contains the validator, generator, definition, and lifecycle components.
The validator contains the URLs for the requirements, definition, and lifecycle metamodule versions.
The generator contains the URLs for the implementation, test, and lifecycle metamodule versions.
The definition contains the name, problem, solution, type, version, author, license, website, and git repository.
The lifecycle contains the packages, config, and monitoring information.
It includes the nodejs, mariadb, and docker versions, username, path, data, and settings information, and latency and availability metrics.


## schema definition with pattern validation for that json


```json
{
  "type": "object",
  "properties": {
    "validator": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "generator": {
      "type": "object",
      "properties": {
        "implementation": {
          "type": "string"
        },
        "test": {
          "type": "string"
        },
        "lifecycle": {
          "type": "string"
        }
      },
      "required": [
        "implementation",
        "test",
        "lifecycle"
      ]
    },
    "definition": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
```
more in file: [schema/environment.json](schema/environment.json)

example of validation for expected data for a GPT
```
"expect": [
        {
            "name": "model",
            "type": "select",
            "label": "Model",
            "required": true
        },
        {
            "name": "prompt",
            "type": "text",
            "label": "Prompt"
        },
        {
            "name": "max_tokens",
            "type": "number",
            "label": "Max Tokens"
        },
        {
            "name": "temperature",
            "type": "number",
            "label": "Temperature"
        },
        {
            "name": "top_p",
            "type": "number",
            "label": "Top p"
        },
        {
            "name": "n_completions",
            "type": "number",
            "label": "N"
        },
        {
            "name": "echo",
            "type": "boolean",
            "label": "Echo"
        }
    ]
```
## How the metamodule json specification can help in software development?

The metamodule json specification can help in software development by providing a unified language for
documenting, validating, and managing software at all stages of the development lifecycle.

It provides a structure for developers to define the properties of their software modules,
such as the name, problem, solution, type, version, author, license, website, and git repository.
It also provides a way to validate the code and documentation against a set of standards.
Finally, it provides a way to manage the software Lifecycle including packages, config, and monitoring information
such as nodejs, mariadb, docker, username, path, data, settings, latency, and availability metrics.
All of these features help to ensure that software is built to the highest quality and meets all the required standards.

## How can help the json build better software requirements specification?


The json build better software requirements specification by providing a standardized language for documenting
and validating the requirements of a software project.
It can be used to define the properties of the software, such as the name, problem, solution, type, version, author, license, website,
and git repository. It also provides a way to validate the code and documentation against a set of standards.
This helps to ensure that the software meets all of the necessary requirements for the project.


## How software developer can start with meta modules?

Software developers can start with meta modules by first becoming familiar with the metamodule json specification
and the different components contained within it. They should then research the different components of the specification
and how they can be used to document, validate, and manage the software. Once they have a good understanding of the specification,
they can start building the software and incorporating the meta modules into their development process.


## How to develop, integrate, and improve the metamodule specification?


Developers can develop, integrate, and improve the metamodule specification by researching the different components
and understanding how they can be used to document, validate, and manage the software.
They should identify areas where the specification can be improved and create new features or improvements to the existing components.
Once they have identified the areas that need improvement, they should develop and integrate the changes into the existing specification.
Finally, they should test and evaluate the changes to ensure that they meet the requirements
and improve the overall software development process.




---


# TODO:

+ metamodule in shell in python
+ validation with many schemas
+ create json section based on generator
+ prepare examples for:
  + schema
  + validator
  + generator


## Start using MetaModule in shell with your project

```bash
curl http://download.metamodule.org
chmod +x mm.sh
mm.sh install
```


## Start Use metamodules

Create **mm.json** file
```bash
mm init
```

### INIT

Create empty validator section
```bash
mm validator create
```

Create empty generator section
```bash
mm generator create
```


### Add to list current list

Download schema and valid all listed sections in a document
```bash
mm validator create "lifecycle" "http://lifecycle.dsdasdadas.org"
```

Download library list and put objects to root **mm.json**
```bash
mm generator create "lifecycle" "http://lifecycle.dsdasdadas.org"
```


### UPDATE ALL

Update validator section based on list
```bash
mm validator update
```

Update generator section based on list
```bash
mm generator update
```

### UPDATE SELECTED

Update validator section based on list
```bash
mm validator update "lifecycle" "http://lifecycle.dsdasdadas.org" "lifecycle2" "http://lifecycle.dsdasdadas.org"
```

Update generator section based on list
```bash
mm generator update "lifecycle" "http://lifecycle.dsdasdadas.org" "lifecycle2" "http://lifecycle.dsdasdadas.org"
```



### Show List current list

Download schema and valid all listed sections in a document
```bash
mm list validator
```

Download library list and put objects to root **mm.json**
```bash
mm list generator 
```



### Show List current list

Download schema and valid all listed sections in a document
```bash
mm validator
```

Download library list and put objects to root **mm.json**
```bash
mm generator
```


Create section based on default
```bash
mm list schema
```

mm remove schema **[part of schema url]**
```bash
mm remove schema *generator*
```



## JSON examples

Create empty validator
```bash
mm create validator 
```
```json
{
  
} 
```

Create validator, add to validator section, create section if not exist
```bash
mm create validator "definition" "http://lifecycle.dsdasdadas.org" 
```
```json
{
  
} 
```

OR

Create empty section without validation
```bash
mm create definition 
```

```json
{
  
} 
```

OR

Create with defaults from generator and add to generator section
```bash
mm create generator "definition" "http://lifecycle.dsdasdadas.org" 
```

```json
{
  
} 
```



## Modularity and Monorepo

+ [All You Always Wanted to Know About Monorepo But Were Afraid To Ask - Tomas Votruba](https://tomasvotruba.com/blog/2019/10/28/all-you-always-wanted-to-know-about-monorepo-but-were-afraid-to-ask/)

Monorepo vs. Multirepo
Single-repo or split-repo?

Monorepo is split into many single-repos, e.g. Symfony/Symfony is split into Symfony/Console, Symfony/Validator etc. Each single-repo repository is read-only. You can change its code via pull-request to the monorepo.
Many-repo

The other approach to manage multiple repositories. 1 package = 1 own repository. Each package has it's own development, tagging and even maintainers. E.g. Doctrine 2 or Nette 2.
Monolith

Monolith ≠ monorepo. Monolith is huge amount of coupled code of 1 application that is hell to maintain.
Why is Monorepo so Awesome?

+ Simplified organization
+ Easy to coordinate changes across modules.
+ Simplified dependencies
+ Single lint, build, test and release process

Tooling
+ Single place to report issues
+ Cross-project changes
+ Tests across modules are run together → finds bugs that touch multiple modules easier

These are cherry-picked reasons from legendary Advantages of Monolithic Version Control. Read it to get deeper insight.



---

+ [edit](https://github.com/meta-module/docs/blob/main/README.md)
+ [meta-module/docs](https://github.com/meta-module/docs)

