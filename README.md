# dropReferenceScraper
This is a simple scraper for "drop reference" website

## License
This project is licensed under the [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.html).
- You are free to use, modify, and distribute the code, but **commercial use is prohibited without explicit permission**.
- Any significant modifications or derived works must credit the original author, **`Yassine EL IDRISSI`**, and must also be distributed under the same license.

# How to use

Use the following commands to export the data to a CSV file:

```bash
python main.py --type "Your type" --model "Your model"
```

Here is the list of types:

- `gpu`
- `cpu`
- `ram`
- `ssd`
- `psu`
- `cm`
- `boitier`
- `ventilation`
- `laptop`
- `mouse`
- `keyboard`
- `screen`

Example :

```bash
python main.py --type "gpu" --model "rtx 3080"
```

File will be saved in csv format like this : `gpu_rtx_3080.csv`