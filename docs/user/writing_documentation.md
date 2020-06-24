
# Writing Documentation
When adding new features to garage, it is important that these features are well-documented and accessible. Garage's high-level docs contain information on workflows and processes that are regularly used by developers and end-users. They are home to various how-to's and examples that help others use garage effectively.

High-level documentation should focus on describing such workflows, or, in the case of newly-added features, describing how these features might be used when running experiments. For code-level documentation such as docstrings and style guides, please see the [CONTRIBUTING.md](https://github.com/rlworkgroup/garage/blob/master/CONTRIBUTING.md).


## Where to Put Documentation
You can choose to update the existing docs under the `docs/user` directory, or create a new page dedicated to the subject you are documenting.

In certain cases, it may be beneficial to include your documentation in a README file in a directory specific to that new feature or workflow. Garage's `docker` folder, for example, contains the main Dockerfile and `entrypoint.sh` scripts that are used to run the docker builds. This folder contains a separate README with details on garage's docker images and how to run them.

## General Guidelines

We suggest going through the documentation to familiarize yourself with how docs are written in garage. We've included a list of do's and don'ts to keep in mind when writing documentation:

### Do's:

Do keep your doc:
 - Self-contained - avoid having users go through multiple pages to understand how to use a feature or become familiar with a workflow.
 -  Accessible - Include examples to help demonstrate a point or feature, and clarify code snippets by providing context.
 - Readable - Make use of markdown styling (see [this page]([https://commonmark.org/help/](https://commonmark.org/help/)) for a markdown cheatsheet) - see the section below for more on styling.

 ### Don'ts:

 - Claim other work as your own. Please cite external sources - you may use footnotes for this purpose.
 - Shy away from pointing to external resources. There are several high-quality online resources that explain various reinforcement learning techniques. We refer users to them all the time, you should too!

Once you've finalized your documentation, submit a pull request and the garage maintainers will review it. Once your PR has been approved, it will be merged into the master branch and available for end-users to read.

## Styling

You can take advantage of styling to make your documentation readable. We recommend you go through the markdown cheatsheet linked above for a complete list of the styles and formatting options available to you. Here, we'll emphasize the use of two important ones:

### Code Blocks
Code blocks and syntax highlighting are effective and simple to use. They highlight code snippets in your doc and make them easy to identify. Use three bat ticks "`" to signify the opening and closing of a code block, and append the code language you're using to the opening bat ticks to enable syntax highlighting:

	```python
		def very_readable(int arg):
	```

Results in :
```python
def very_readable(int arg):
```
You can also use one bat tick for inline code snippets, class references, or directory paths:


``you can `cd`  into `~/garage/data/` `` :   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; you can `cd` into `~/garage/data/`


### Sphinx

Our documentation pages are built with Sphinx, which means you can render more complicated shapes within text. Garage docs mostly use the Sphinx `:math:` directive to render shapes and symbols in math equations. [This](https://github.com/rlworkgroup/garage/blob/master/CONTRIBUTING.md#docstrings) section in the `CONTRIBUTING.md` contains various examples that demonstrate how this directive should be used.

 We specifically use this when specifying shapes of input and output tensors in docstrings (and you should too), but we've included this here incase you need to specify tensor shapes in your doc.
