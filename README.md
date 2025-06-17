# SPONGE
## Splicing-factor activity Prediction based On Network and Global splicing Events

SPONGE is a computational pipeline for identifying the activity of splicing factors (SFs). It integrates CLIP-seq peaks, motifs, and alternative splicing (AS) data to construct a splicing regulatory network, and infers SF activities using regression modeling.
![image](https://github.com/user-attachments/assets/49c5a43b-abe2-4a6a-9425-f6ca80f76c04)



### Installation

#### Option 1. Install SPONGE through pip [recommended]
```bash
conda create -n SPONGE python=3.8
pip install SPONGE
```

#### Option 2. Local installation
```bash
conda create -n SPONGE python=3.7
git clone https://github.com/liuyilei8969/SPONGE.git
cd SPONGE
pip install .
```


### Usage
1. Identify targets of a splicing factor
bash
复制
编辑
python src/SPONGE/findtarget.py \
  --rmats test/findtarget/input/shQKI_rmats.txt \
  --clip_peaks test/findtarget/input/QKI_CLIP_sig_peaks.bed \
  --ref_genome REF_GENOME \
  --rbp_motif data/Motif.txt \
  --rbp_name QKI \
  --cell_line HepG2 \
  --output OUTPUT_DIR
2. Construct SF-to-AS event network
bash
复制
编辑
python src/SPONGE/construct_network.py \
  --Target_dir OUTPUT_DIR \
  --threshold 0.6 \
  --DE_dir test/expr/ \
  --output QKI_network.gexf
3. Infer splicing factor activity
bash
复制
编辑
python src/SPONGE/calculate_activity.py \
  --diffAS test/diffAS/HepG2_QKI_rmats.txt \
  --network QKI_network.gexf \
  --output activity_scores.txt
🧪 Test Data
Example input files are provided in the test/ directory:

rMATS output (splicing events)

CLIP-seq peak files

Motif files

Expression values (for network weighting)

📘 Requirements
Python >= 3.8

Packages: pandas, numpy, networkx, scikit-learn, argparse

You can install them with:

bash
复制
编辑
pip install pandas numpy networkx scikit-learn
