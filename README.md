![https://logo.metamodule.org/1/cover.png](https://logo.metamodule.org/1/cover.png)

# MetaModule Documentation [docs.metamodule.org](http://docs.metamodule.org)

pisząc książkę o hipermodularyzacji musiałem stworzyć specyfikację metamodułów, które są
specyfikacją czegoś co da się określić, czyli procesu, usługi, oprogramowania, roli w zespole...
to taka cyfrowa reprezentacja definicji modelu modułu


## install requirements
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





## TODO:

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
