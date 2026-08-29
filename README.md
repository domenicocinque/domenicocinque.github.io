# Writing posts

New posts can be written in Markdown; existing handwritten HTML posts do not need to change.

## Create a post

Copy the example and give it the URL you want:

```sh
cp content/posts/example.md.example content/posts/my-new-post.md
```

The filename becomes the URL. For example, `my-new-post.md` is generated at
`posts/my-new-post/index.html` and is available at `/posts/my-new-post/`.

Each post starts with metadata:

```yaml
---
title: My new post
date: 20 Mar, 2026
---
```

Write normal Markdown below it. Fenced code blocks, tables, images, and `$...$` /
`$$...$$` math are supported.

## Build and preview

Install [Pandoc](https://pandoc.org/installing.html) once. On macOS:

```sh
brew install pandoc
```

Then build the posts:

```sh
just build
```

Preview the complete site:

```sh
just serve
```

Generated HTML is committed to the repository along with its Markdown source, so GitHub
Pages can continue serving this repository without any deployment changes.

Finally, add a link for the post to `index.html`. Post-list generation can be automated
later if desired; keeping it manual for now avoids changing the existing external and
handwritten entries.

## Images

Put post-specific images under the generated post directory, for example
`posts/my-new-post/images/chart.png`, then reference them in Markdown as:

```md
![A chart](images/chart.png)
```

The build only replaces `posts/my-new-post/index.html`; it leaves the image directory
alone.
