# Privacy Engineering Handbook

We live in a world where automated information processing is part of our
everyday life. In many cases, the information that these software systems
process belong to individuals, it is personal data.

## What Is Privacy?

We will rely on the following basic definition of privacy in this handbook[^1]:

> Privacy is the ability of an individual or group to seclude themselves or
> information about themselves, and thereby express themselves selectively. 

While this definition seems rather broad on first reading, it immediately allows
us to derive several rights that a person needs to possess in order to ensure
her privacy: For example, she can only seclude information about herself if she
knows that this information exists, what it is comprised of and how, by whom
and for what it is used. In addition of knowing about how her information is
processed, she also needs to have the agency to request that specific information
about her is no longer processed or that it even is deleted.

## Privacy Laws

The idea of privacy alone is not very useful without a way to enforce it. Over
the last decades, many laws have been introduced to formalize the right to
privacy and integrate it into a formal legal framework. Privacy legislation is
still a very young field: The first dedicated privacy law was introduced less
than 50 years ago, in 1973's Sweden[^2]. In the years after that, many other
countries passed privacy laws. It is no coincidence that these laws came up
around the time that computer-based information processing became widespread:
With more and more personal and sensitive information being processed by
software-based systems, the need to control this processing quickly became
obvious. Therefore we can safely assume that privacy laws will become more and
more prevalent around the world and that they will keep evolving at a rapid
pace to keep up with our exponentially evolving information processing
abilities.

To accomodate the wide variety of privacy laws that exist today we have chosen
the following approach in this book: In each section, we will first discuss
a specific privacy-enhancing technique without without referring to a specific
legal framework. Then, we will add sections for each specific privacy law we
cover and explain the specific role of this technique within that law. Like
this, you can pick just the sections that are relevant for you. Currently this
handbook includes sections for the following privacy laws:

* The EU  General Data Protection Regulation (GDPR)
* The California Consumer Privacy Act (CCPA)
* The Singapore Personal Data Protection Act (PDPA)

We hope to include more laws in the future.

## Engineeering Privacy

From these rights we can in turn derive a set of requirements
for software systems that process personal information.

[^1]: [Privacy - Wikipedia](https://en.wikipedia.org/wiki/Privacy)
[^2]: [Privacy Law - Wikipedia](https://en.wikipedia.org/wiki/Privacy_law)