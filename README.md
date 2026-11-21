# Low Res Materials
Free low resolution materials for games and other projects.</br>
You can use all the things on this repository in any project for free and without any attribution.</br>
Licensed under [CC0-1.0 license](LICENSE)</br>
Some photos in low res looks better, some worse ;)</br>

<h2>How is it made?</h2>
We photograph walls, ground, and surfaces, and then use Python scripts to rename new source images and generate square textures at lower resolutions.
The processing scripts were created with Gemini AI, while the source photographs are taken by me and contributors.

## Tools & Automation

- **Python & Pillow (PIL)** – renames new files in `Original-Photos/` using two random English words from `data/words.txt`, clears output directories, and crops/scales textures into squares (`64x64`, `128x128`, and `256x256` in `64p`, `128p`, and `256p`).
- **GitHub Actions** – automatically runs the renaming and texture-processing scripts on updates to source images and commits the renamed originals and generated textures.
- **License scope** – this license (CC0 1.0 Universal) applies only to the contents of this repository and does not alter the licenses of third-party tools, runtimes, or libraries used to build or run it.


## Star History

<a href="https://www.star-history.com/?repos=open-cake-materials%2Flow-res-materials&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=open-cake-materials/low-res-materials&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=open-cake-materials/low-res-materials&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=open-cake-materials/low-res-materials&type=date&legend=top-left" />
 </picture>
</a>
