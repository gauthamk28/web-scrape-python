# Web-Scrape-Python
This repository is inspired from the [play-scrape](https://github.com/RiccardoAncarani/play-scrape) . It was giving output in JSON format and only Italian reviews were generated.I made some changes inorder to  scrape English reviews and also made the output in both **csv** and **JSON** formats.
Credits goes to [RiccardoAncarani](https://github.com/RiccardoAncarani). And the analysis with graphs was inspired from [textblob-sentiment-analysis](https://github.com/stepthom/textblob-sentiment-analysis/blob/master/doAnalysis.py) by [stepthom](https://github.com/stepthom)

![Cleaned scraped output sample](review%20cleaned.PNG)

### Usage:
```dos
python re_scrape.py --pages <pages> --id <app_id> --output <outfile.json>
```
