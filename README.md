[Deutsche Version](README-DE.md)

# Introduction

Welcome! This is a community-created information portal about the European
General Data Protection Regulation (GDPR). The goal of this project is to
provide comprehensive, accessible and relevant information that helps people,
organizations and companies to better understand and comply with the GDPR.

Currently, the project contains the following components:

* The GDPR law texts in various formats, including HTML, PDF and YAML.
  We want to make it easy for people to use these texts in their projects
  and therefore provide annotated, machine-readable versions that can be
  easily processed.
* Technical articles and guidelines that describe specific requirements of the
  GDPR and how to implement them in practice.
* A discussion board where people can ask and answer questions regarding the
  GDPR (hosted externally on Discourse).

# Contributing

This is a community portal, so please contribute and help us to make it better!
When contributing, please follow this process:

* Download and sign the appropriate contributor license agreement for
  [individuals](clas/cla_gdpr_community_portal_individual.pdf) or
  [entities](clas/cla_gdpr_community_portal_entity.pdf)
  (e.g. companies, organizations). Send the signed agreement (together with
  your Github username) [to us via e-mail](#questions)
  and we'll send you back a version signed by us. The agreement will remain
  confidential, we will add your Github username to our public list of contributors
  though to make it easy to verify future contributions by you. Please note that
  we are not able to accept any contribution from you before you sign the
  agreement as it creates risk not only for us but for all people and
  organizations that might use original content from this project.
* For larger contributions (e.g. new articles) please first open a Github issue
  and write a short proposal, so that the community can provide feedback
  before you get started. This will ensure that your contribution really adds
  value and has a high probability of making it into the portal.
* For smaller edits and improvements you can directly do the work and open
  a pull request when you're done.
* Start working on your improvement. Ideally, you will create a fork of this
  project and create a new branch in that fork where you perform your work.
* When you're done with your improvement (or when you want some feedback on
  an initial version), you open a pull request where you describe what you
  did (ideally linking back to the Github issue you created). If you just
  want to get some feedback but your work is not yet finished, you can add
  a "WIP" prefix to the title of your pull request to indicate this.
* The community will provide feedback and help you to finalize your
  improvement.
* When all open questions and the collected feedback is addressed, we merge
  your improvement into the master branch and publish it on
  [our portal](https://gdpr.dpkit.com).

The following sections discuss specific types of materials on this portal
that you can contribute to.

## Wiki

Wiki pages are a great place to collect relevant information about an
article, definition, topic or recital. Currently we do not have a fixed
structure for this as we still try to figure out what's the best format, so
please feel free to structure you content as you see fit and submit it
for discussion early and often.

To create a new Wiki page for an article, go to the relevant source directory
(e.g. `src/en/gdpr/chapters/1/sections/0/articles`) and create a file calles
`[article-number]-wiki.md` (e.g. `1-wiki.md`). The content of the file will
be picked up during the generation of the site and added to the corresponding
article.

## Summary

An article summary should help people to quickly grasp the essence of the
article without being overwhelmed by legalese. Summaries should be short
(obviously) and be writen in an accessible language. Feel free to make use
of bullet lists and emphasis (e.g. **bold text**) but try to keep it simple.

To create a new summary page for an article, go to the relevant source directory
(e.g. `src/en/gdpr/chapters/1/sections/0/articles`) and create a file calles
`[article-number]-summary.md` (e.g. `1-summary.md`). The content of the file will
be picked up during the generation of the site and added to the corresponding
article.

# Contributors

The following Github users/organizations are verified contributors that have
signed the contributor license agreement:

* adewes

# Building

The HTML contents of this project are built using the  static website builder. 
To build the website and documents, you will need to install the following
pre-requisites:

* Python 3
* Ruby-Sass
* [PrinceXML](https://www.princexml.com) (only if you want to generate PDFs)

On Ubuntu, you can install these packages as follows:

    # required to build the docs / website
    sudo apt install python3 python3-pip
    # required to generate the CSS
    sudo apt install ruby-sass
    # only required if you want to use the "watch commands"
    sudo apt install inotify-tools
    # to create a virtual environment
    sudo pip3 install virtualenv

You can then create a virtual environment (recommended) and install the
required Python packages:

    virtualenv --python python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

To download and install PrinceXML, follow the instructions on their website.

After installing all the pre-requisites, you can run the following command
to build the website:

    make html

To generate the PDF documents, run the following command:

    make docs

Please not that in order to build the PDFs you will first need to install
[PrinceXML](https://www.princexml.com) (if you want to use the PDFs for
commercial purposes you will need to buy an appropriate license).
We (7scientists GmbH) generate the PDFs in the production version via a
subscription to the [DocRaptor] (https://www.docraptor.com) service.

## Advanced Build Steps

When developing locally it is convenient to automatically rebuild
the website / docs after each change. You can do this by running the
following command:

    # for the website
    make watch-html

    # for the documents
    make watch-docs

To re-generate the law texts from their raw source (which should normally
never be necessary), run the following command:

    make law-texts

# License

The GDPR community portal consists of **original resources** (i.e. text,
code or images created by verified contributors of this project) as well as **third-party
resources** (e.g. European law texts, images and code). Here, the term **resource**
includes but is not limited to texts, images, code and any other assets that
are provided as part of this project.

All original resources that are not software code (see below for that) are licensed under a 
[**Creative Commons Attribution-ShareAlike (CC BY-SA)**](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
license, which allows commercial and non-commercial use of the resources. 
The full text of the license can be viewed on the linked website and is included
with this project in [German](LICENSE-DE)
and [English](LICENSE-EN). If you
use original resources from this project you need to attribute them to this
project in the following way:

* For printed materials (e.g. flyers, books, brochures, ...), you need to
  include the title and a link to the GDPR community portal (https://gdpr.dpkit.com)
  in your title page or first page.
  The information has to be placed prominently and needs to include a notice
  about the original license as stated in the CC-BY-SA license terms.
* For online content you need to include the title and a link to the GDPR
  community portal (https://gdpr.dpkit.com) on each page that contains
  resources from this project.

Please note that the license agreement does not extend to third-party resources
and resources, so please carefully read the section below before you re-use
any third-party resources from this project.

Original software code published as part of this project is released under a
[BSD 3 Clause License](LICENSE-CODE).

## Exceptions / Custom Licences

If you want to use original resources from the GDPR community portal in a way
that is not allowed by the CC BY-SA license, please [contact us][#questions]
and describe your use case. We might be able to grant you a custom license then
if you make sure that any added value will be contributed back to this project.

## Third-Party Resources & Licenses

The following third-party resources have been used to build this community portal:

* [PrinceXML](https://www.princexml.com/) PrinceXML (via DocRaptor) was used
  to generate the PDF materials. You may use their free version for
  non-commerical purposes, if you want to generate custom PDFs for commercial
  purposes you will need to buy a proper license.
* [Beam-Up](https://pypi.org/project/beam-up/)
* [Bulma.io](https://www.bulma.io): A MIT-licensed Flexbox CSS framework 
* [Preact.js](https://preactjs.com/): A MIT-licensed frontend library.
* Fonts: [IBM Plex](https://github.com/IBM/plex), [Open Sans](https://github.com/google/fonts/tree/master/apache/opensans) and [Roboto](https://github.com/google/roboto)
* [Futuro Icons by Bloomicon](http://bloomicon.com/): 7scientists GmbH acquired
  a license for using the icons on the DP-Kit websites(s). If you want to
  re-use the icons for other purposes than this project you will need to
  buy a license yourself.
* Logos: [Creative Commons](https://creativecommons.org/), [Octicon](https://en.wikipedia.org/wiki/File:Octicons-mark-github.svg)
* [European Laws from EUR-Lex](https://eur-lex.europa.eu/content/legal-notice/legal-notice.html#droits)

We take intellectual property rights very serious. If you think that any
material on this project may infringe on your copyright or the copyright of a
third party, please [contact us](#questions) or open an issue.

# Questions?

If you have questions regarding this project here's how to get answers:

* If your question could be of interest to other people as well please create
  an issue in our [issue tracker](https://github.com/DPKit/gdpr-portal/issues), as
  this will allow the community to help you and will make the answer accessible
  to other people that might have the same question.
* If you want to ask a question but do not want to do so publicly, feel free
  to send us an e-mail to **gdpr-portal@dpkit.com**

Please do not create issues for GDPR-related questions, as this is what our
discussion board is for!

# Imprint

This project is maintained by 7scientists GmbH (https://7scientists.com).