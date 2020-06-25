# Our Privacy & Security Engineering Framework

At KIProtect we have helped numerous organizations to implement secure,
privacy-focused data workflows. To make this process more efficient and reduce
implementation and maintenance effort, we have systematized our process and
built a software framework to automate as much of it as possible. This helps
our customers and users to avoid spending time to engineer solutions to problems
that have been solved already. And while we're arguably still far away from our
ultimate goal to completely automate security and privacy engineering, we are
already able to automate many of the most tedious and error-prone processes.
The following paragraphs explain how we do this.

## Regulatory Scope

Privacy and security requirements can vary greatly based on country and business
sector. Building a framework that can work in all possible environments is
challenging, but possible. To make this work, we kept the core of our software
flexible and extensible. This enables us to implement universal privacy-enhancing
transformations like pseudonymization and anonymization and complement them with
functionality tailored to specific regulatory environments.

## Privacy & Security Modeling Primitives

KIProtect models privacy and security aspects of data flows using a set of
models, which we will discuss in the following sections. Here's the list:

* **Source**: A source from which data items are loaded, such as a database or CSV file.
* **Stream**: A stream of uniform data items that we want to process and use.
* **Configuration**: A specific configuration applied to a data stream.
* **Action**: A specific action performed on a data item, such as a pseudonymization. Actions can be performed individually or as part of a configuration.
* **Destination**: A destination to which data items should be sent, such as a database or CSV file.

In addition, we use the following primitives to model data types, ownership (or subject rights) as well as
consent and processing purposes for data items:

* **DataSchema**: A schema that describes the content of a group of data items, consisting of a set of attributes. Data schemas can be attached to sources, destinations, streams and configurations.
* **DataOwner**: A person or entity that "owns" a set of data items, such as a data subject as defined by the GDPR or a company that owns a non-personal dataset.
* **Identifier**: A concrete data value that identifies a data owner, such as an e-mail address or name.
* **Purpose**: A purpose for which a given configuration exists.
* **Consent**:  A consent that a data owner has given (or withdrawn) regarding the processing for a specific purpose.
* **Request**: A request filed by a data owner regarding data items, such as a data portability request of a data subject as defined by the GDPR.

Finally, there are higher-level primitives that model data flows for more specific use cases such as
machine learning or analytics. They make use of the basic primitives above but hide much of their
complexity from the end user (you), which makes it much easier to implement privacy and security
workflows without specifying each detail. In addition, our **privacy & security blueprints** make it
easy to solve common privacy and security engineering use cases using KIProtect without too much
integration work. 

So before we dive into the practical aspects of privacy and security engineering with KIProtect, let's have a brief look at each of the primitives!

## Source

## Stream

## Configuration

## Action

## Destination

## DataSchema

A data schema

## DataOwner

## Identifier

## Purpose