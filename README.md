SPONGE
Splicing-factor activity Prediction based On Network and Global splicing Events

SPONGE is a computational pipeline for identifying the activity of splicing factors (SFs) based on their binding information and large-scale splicing changes, especially in perturbation conditions (e.g., knockdown or overexpression). It integrates CLIP-seq peaks, motif matches, and alternative splicing (AS) data to construct a splicing regulatory network, and infers SF activities using regression modeling.

📦 Project Structure
bash
复制
编辑
SPONGE/
├── src/                    # Source code
│   └── SPONGE/
│       ├── findtarget.py           # Identify SF-target splicing events
│       ├── construct_network.py    # Build SF-to-AS event regulatory network
│       └── calculate_activity.py   # Infer SF activity using regression
├── test/                   # Test inputs and example scripts
│   └── findtarget/
│       └── input/          # Example rMATS, CLIP-seq, motif input files
├── data/                   # Motif definitions or annotation files
├── README.md               # This file
├── LICENSE                 # License file
└── pyproject.toml          # Python project metadata
🚀 Installation
You can install the dependencies manually or use a virtual environment.

bash
复制
编辑
git clone https://github.com/liuyilei8969/SPONGE.git
cd SPONGE
pip install -r requirements.txt
(Optional) If you use pyproject.toml, install via hatch or poetry.

⚙️ Usage
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
