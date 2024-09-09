# Nordic Guidelines for Mathematical Content in HTML Files, Using MathML

## Introduction

This guidelines document is a joint effort between the (mostly) Nordic agencies dedicated to providing accessible literature in different formats – e.g. talking books, braille, and accessible e-books – to children and adults with various reading impairments or special needs. The participating organisations are [Celia](https://www.celia.fi/), [HBS](https://hbs.is/), [MTM](https://mtm.se), [NB](https://www.nb.no/), [Nota](https://nota.dk/), [SBS](https://www.sbs.ch/), [SPSM](https://www.spsm.se/), and [Statped](http://statped.no/).

Making book content accessible starts in well-structured and granular semantic markup using available markup and accessibility standards. When it comes to mathematics, the quality of the markup is essential in order for assistive technology to be able to correctly and unambiguously convey the information to the reader. It is not enough that the visual representation of a mathematical expression looks correct, the structure of the expression needs to be correctly expressed in the markup. The purpose of this document is to give further guidance in how to properly construct mathematical expressions that will give any user a correct understanding of the expression.

The basis of this document is the [MathML Core specification](https://www.w3.org/TR/mathml-core/). The aim is to provide a better understanding of how to use the MathML standard in the context of the services provided by the Nordic Agencies. The target audience of the document is mainly the Nordic agencies’ contracted EPUB 3 suppliers, but the guidelines will also be used by staff at the Nordic agencies, other vendors and interested parties, etc.

## When To Use MathML <!--- maybe change wording later -->

As a general rule, every mathematical or scientific expression that can't be rendered with standard HTML must be captured as MathML, whereas things that can be rendered with standard HTML, like numbers, units, single Unicode characters and even simple arithmetic expressions, should be captured as HTML. However, there may be a valid point to use MathML a bit more extensively in some cases, especially in STEM content.    

### Numbers

Plain numbers, with or without decimal points or commas, are not necessary to mark up with MathML markup. They are required to be captured as plain text, formatted as in the source material. Points, commas, spaces etc. must be preserved.

### Numbers With Units

In general, numbers with attached units do not require MathML markup. The units should in most cases be captured as plain text using Unicode for any Greek symbols and `<sup>` for any exponents. However, in STEM content the Ordering Agencies may require MathML markup in order for text-to-speech output to be consistent throughout the content.

### Single Variables or Symbols

Single occurrences of variables, normally displayed in italics, constants or other symbols do not require MathML markup. They can in most cases be captured as plain text using the proper characters or Unicode symbols. If they are displayed in italics in the source material they should be styled accordingly, using the standard HTML elements.

### Simple Arithmetic Expressions in Linear Form

Mathematical expressions, such as calculations, functions, equations etc., are in general required to be marked up using MathML. However, if there are one or a few isolated simple expressions in a non-STEM context, they may be captured as plain text as long as the expressions are linear and just simple arithmetic expressions such as "1 + 1 = 2" or "3 - 1 = 2". Anything more complex or containing non-standard characters or symbols is required to be captured as MathML.

## MathML Fundamentals

### The Top-Level `<math>` Element

### Namespace

### alt-attributes

A `<math>` element has two different alt-attributes:
1. `alttext`
2. `altimg`.

The attribute `alttext` is used to provide an **alternative text** fallback for mathematical content when a reading system doesn't support MathML markup. Usually it is ASCIIMath or LaTeX as these formats are well known in STEM subjects. The Ordering Agency may decide which kind of content should be in the `alttext` attribute.

The attribute `altimg` is used to provide an **alternative image** fallback for mathematical content. Usually this is just a screenshot of the rendered equation. It should used with caution, since MathML Core does not support the `altimg` attribute. It is also only a visual fallback, because you can't provide an alternative text for the fallback image. The Ordering Agency may decide if the attribute is used.

### Block vs Inline

<!--- displaystyle="true" for block -->

### Presentation vs Content MathML

<!--- Next section is completely based on Presentation MathML -->

## Basic Markup Structure

### Token Elements

#### `<mn>`

The `<mn>` element is used to mark up all kinds of numeric characters. This also includes decimal and thousand separators. They shouldn't be mark up separate from the number.

There are different ways to mark up the decimal and thousand separators based on the publication. Follow the mark up of the publication unless specifically told otherwise by the Ordering Agency.


For example using 
- comma as a decimal separator: `<mn>3,14</mn>`
- non-breaking space as a thousand separator: `<mn>89&nbsp;000</mn>`
- period as a decimal separator: `<mn>2.74</mn>`
- comma as a thousand separator: `<mn>19,050</mn>`.

#### `<mo>` for operators

The `<mo>` element is used to denote operators. The definition of an operator is loose and it can mean the actual mathematical operators plus (+), minus (&minus;), times (&centerdot;) and divided by (/).

In MathML it also means different parentheses. For example the parenthesis `<mo>(</mo>` and curly bracket `<mo>{</mo>`.

The same character can be used in a different meaning based on the context. For example the comma can be part of a number, but in a sequence the comma is an operation.

For example the sequence $\{1,2,3,...\}$ written in MathML:
```html
<mo>{</mo>
<mn>1</mn>
<mo>,</mo>
<mn>2</mn>
<mo>,</mo>
<mn>3</mn>
<mi>...</mi>
<mo>}</mo>
```

#### `<mi>` element for variables and functions

The `<mi>` element is used to denote variables and other identifiers. An identifier can be just one letter of symbol such as a variable $\alpha$ or $x$, but it can also be multiple letters such as function names: $\tan$, $\sin$ or $\log$.

The ellipsis or three dots &#x2026; are also an identifier `<mi>&#x2026;</mi>`.

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

### Tabular Math (Sami)

Math can be presented in a table-like structure and MathML has its own markup to handle this.

If there is an actual data formatted in a publication, use the HTML element `<table>` and not the MathML element `<mtable>`.

#### Table or Matrix, `<mtable>`

Use a HTML `<table>` when the it's possible. It should be used with presenting data and when MathML isn't needed (as per section When To Use MathML). Example:

![Example of an 3 times 3 HTML table with just numbers in the cells.](images/html-table.png)

```html
<table>
    <tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    </tr>
    <tr>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    </tr>
    <tr>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    </tr>
</table>
```


It is okay to mix HTML and MathML markup inside the HTML `<table>`. Example:

![Example of an 3 times 3 HTML table with numbers and two fractions.](images/html-table-with-mathml.png)

```html
<table>
    <tr>
    <td>
        <math>
            <mfrac>
                <mn>2</mn>
                <mi>x</mi>
            </mfrac>
        </math>
    </td>
    <td>2</td>
    <td>3</td>
    </tr>
    <tr>
    <td>4</td>
    <td>5</td>
    <td>
        <math>
            <mfrac>
                <mn>5</mn>
                <mrow>
                    <mn>2</mn>
                    <mo>&#x2062;</mo>
                    <mi>x</mi>
                </mrow>
            </mfrac>
        </math>
    </td>
    </tr>
    <tr>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    </tr>
</table>
```



If there is mathematical notation that can't be achieved with just an HTML `<table>`, then use MathML `<mtable>`.

Usually, if there are large parentheses or brackets that need to wrap around a tabular structure, use MathML `<mtable>`. This can be a matrix or a determinant.


For example a puzzle may be presented in a table ...

Matrices are usually a table-like structures and the element `<mtable>` should be used.

#### Row in Table or Matrix, `<mtr>`

#### Entry in Table or Matrix, `<mtd>`

##### Colspan and Rowspan

#### Labeled Row in Table or Matrix, `<mlabeledtr>` <!--- needs investigating -->

## Context-Based Applications <!--- maybe change wording later -->

### Sums, Products, Integrals etc.

### Invisible Operators

Insivible operators are used when the meaning of an equation would be ambigious. For example $a(x+1)$ might be the function $a$ of $x+1$ or then it could be the multiplication between a and $(x+1)$.

Using invisible operators makes the markup unambigious:

- insivible multiplication: `&#x2062;`
- invisible function application: `&#x2061;`
- invisible plus: `&#x2064;`
- invisible comma: `&#x2063;`

(Can be deleted later) Source: [MathML 4 "Invisible operators"](https://www.w3.org/TR/mathml4/#presm_invisibleops).

### Systems of Equations (Sami)

### Chemistry

<!--- these are examples, must fill section with more -->

## Special Content Requirements

### Special Characters

### Typefaces

### HTML Inside a Math Expression

## Resources

Text
