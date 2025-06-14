python src/SPONGE/find_target.py \
--rmats test/find_target/input/shQKI_rmats.txt \
--clip_peaks test/find_target/input/QKI_CLIP_sig_peaks.bed \
--ref_genome REF_GENOME \
--rbp_motif data/Motif.txt \
--cell_line HepG2 \
--rbp QKI \
--output test/find_target/output \
--max_iter 1000 \
--tol 1e-4
