# Nordic Guidelines for Mathematical Content in HTML Files, Using MathML

## Introduction

This guidelines document is a joint effort between the (mostly) Nordic agencies dedicated to providing accessible literature in different formats – e.g. talking books, braille, and accessible e-books – to children and adults with various reading impairments or special needs. The participating organisations are [Celia](https://www.celia.fi/), [HBS](https://hbs.is/), [MTM](https://mtm.se), [NB](https://www.nb.no/), [Nota](https://nota.dk/), [SBS](https://www.sbs.ch/), [SPSM](https://www.spsm.se/), and [Statped](http://statped.no/).

Making book content accessible starts in well-structured and granular semantic markup using available markup and accessibility standards. When it comes to mathematics, the quality of the markup is essential in order for assistive technology to be able to correctly and unambiguously convey the information to the reader. It is not enough that the visual representation of a mathematical expression looks correct, the structure of the expression needs to be correctly expressed in the markup. The purpose of this document is to give further guidance in how to properly construct mathematical expressions that will give any user a correct understanding of the expression.

The basis of this document is the [MathML Core specification](https://www.w3.org/TR/mathml-core/). The aim is to provide a better understanding of how to use the MathML standard in the context of the services provided by the Nordic Agencies. The target audience of the document is mainly the Nordic agencies’ contracted EPUB 3 suppliers, but the guidelines will also be used by staff at the Nordic agencies, other vendors and interested parties, etc.

## When To Use MathML <!--- maybe change wording later -->

## MathML Fundamentals

### The Top-Level `<math>` Element

### Namespace

### alt-attributes

### Block vs Inline

<!--- displaystyle="true" for block -->

### Presentation vs Content MathML

<!--- Next section is completely based on Presentation MathML -->

## Basic Markup Structure

### Token Elements

#### `<mn>`

#### `<mo>`

#### `<mi>`

#### `<mtext>`

### General Layout Schemata

#### `<mrow>`

#### `<mfrac>`

#### `<msqrt>` and `<mroot>`

#### `<mpadded>` <!--- test with MathCAT first -->

### Script and Limit Schemata

#### Subscripts and Superscripts, `<msub>`, `<msup>`, `<msubsup>`

#### Underscripts and Overscripts, `<munder>`, `<mover>`, `<munderover>`

#### Prescripts and Postscripts, `<mmultiscripts>`

### Tabular Math

#### Table or Matrix, `<mtable>`

#### Row in Table or Matrix, `<mtr>`

#### Entry in Table or Matrix, `<mtd>`

##### Colspan and Rowspan

#### Labeled Row in Table or Matrix, `<mlabeledtr>` <!--- needs investigating -->

## Context-Based Applications <!--- maybe change wording later -->

### Sums, Products, Integrals etc.

### Invisible Operators

### Systems of Equations

### Chemistry

<!--- these are examples, must fill section with more -->

## Special Content Requirements

### Special Characters

### Typefaces

### HTML Inside a Math Expression

## Resources

Text
