# RAISE
## RBP Activity Inference from Splicing Events
RAISE is a computational pipeline for identifying the activity of RNA-binding proteins (RBPs). It integrates CLIP-seq peaks, motifs, and alternative splicing (AS) data to construct a splicing regulatory network, and infers RBP activities using regression modeling. 
<img width="1069" height="1252" alt="image" src="https://github.com/user-attachments/assets/5e26d81a-fa07-4f7e-bd9d-556d5479ed43" />







### Installation   
RAISE is compatible with most Linux operating systems and requires a Python 3.8+ environment. RAISE can be installed in under 1 minute on a modern desktop or server CPU. Installation time may vary depending on internet connection speed.
#### Option 1. Install RAISE through pip [recommended]
```bash
conda create -n RAISE python=3.8
conda activate RAISE   
pip install RAISE-RBP
```

#### Option 2. Local installation
```bash
conda create -n RAISE python=3.8
conda activate RAISE  
git clone https://github.com/liuyilei8969/RAISE.git
cd RAISE
pip install .
```

#### Option 3. Download precompiled binaries (Windows / macOS)

For users who prefer not to install Python dependencies, precompiled versions of RAISE are available for **Windows** and **macOS**.  
> ⚠ Currently, only the **default splicing regulatory network** is supported when using these binaries.

1. Download the appropriate binary from the [Releases page](https://github.com/liuyilei8969/RAISE/releases).
   - Windows: `RAISE-0.1.3-Windows.exe`
   - macOS: `RAISE-0.1.3-macOS.app.zip`
     
2. Run the application:  
   - **Windows:** double-click `RAISE-0.1.3-Windows.exe`  
   - **macOS:** double-click `RAISE-0.1.3-macOS.app.zip` (may require waiting a few seconds for the GUI to launch)

3. Upload your differential splicing file and click **Calculate Activity** to run the analysis.
<img width="2136" height="463" alt="image" src="https://github.com/user-attachments/assets/0b65abdd-1a4e-448d-b5cb-09c989d74e2c" />



### Usage
#### 1. Identify targets of an RBP
```bash
usage: find_target [-h] --rmats RMATS --clip_peaks CLIP_PEAKS --ref_genome REF_GENOME --rbp_motif RBP_MOTIF --cell_line CELL_LINE --rbp RBP --output
                      OUTPUT [--max_iter MAX_ITER] [--tol TOL] [--use_motif True/False] [--use_clip True/False]

Infer RBP targets using motif, CLIP peaks, and PSI changes.

options:
  -h, --help                             show this help message and exit
  --rmats RMATS                          Input rMATS SE.MATS.JC.txt file.
  --clip_peaks CLIP_PEAKS                Input CLIP peaks BED file.
  --ref_genome REF_GENOME                Reference genome in FASTA format.
  --rbp_motif RBP_MOTIF                  RBP motif file with two columns: RBP and motif.
  --cell_line CELL_LINE                  Cell line name, used to label the output file.
  --rbp RBP                              Target RBP name.
  --output OUTPUT                        Output directory.
  --max_iter MAX_ITER                    Maximum number of EM iterations.
  --tol TOL                              Convergence threshold for EM.
  --use_motif                            Use motif features in EM.
  --use_clip                             Use clip features in EM.
```
For a single RBP, it requires approximately 20 ms of CPU time on a modern desktop or server CPU.    

#### 2. Construct RBP-AS network
```bash
usage: construct_network [-h] --Target_dir TARGET_DIR [--threshold THRESHOLD] --DE_dir DE_DIR --output OUTPUT

Build a splicing regulatory network from target predictions and RBP expression changes.

options:
  -h, --help                             show this help message and exit
  --Target_dir TARGET_DIR                Directory containing RBP target result folders
  --threshold THRESHOLD                  Minimum conditional probability P(T|S,M,C) to include interaction (default: 0.6)
  --DE_dir DE_DIR                        Directory containing RBP expression change files
  --output OUTPUT                        Path to output GEXF file for the constructed network
```
#### 3. Infer RBP activity
```bash
usage: calculate_activity [-h] --diffAS DIFFAS --network NETWORK --output OUTPUT

Infer RBP activity from a splicing regulatory network using ridge regression.

options:
  -h, --help                             show this help message and exit
  --diffAS DIFFAS                        Path to the rMATS differential splicing results file
  --network NETWORK                      Path to the splicing regulatory network
  --output OUTPUT                        Output file for inferred RBP activity scores
```
It requires approximately 10 ms of CPU time on a modern desktop or server CPU. The actual performance may vary depending on factors such as I/O speed, memory speed, and CPU capabilities.  


### Example & Test
Examples are provided in the test/ directory: https://github.com/liuyilei8969/RAISE/tree/main/test     
Data are provided in the data/ directory for users' convenience: https://github.com/liuyilei8969/RAISE/tree/main/data   
We also construct a database RAISEDB for RBP splicing target search: https://liuyilei8969.github.io/RAISEDB/
   
Note: All differential splicing results should be provided in the rMATS format. For users' convenience, we also provide scripts to either convert data into this format or perform a simple differential splicing analysis using a limma test.


### Requirements
Operating system: Linux  
Python >= 3.8  
Packages: pandas, numpy, networkx, scikit-learn, argparse, Bio, pybedtools

