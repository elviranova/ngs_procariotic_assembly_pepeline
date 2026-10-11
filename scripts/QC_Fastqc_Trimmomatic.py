#Workflow: terminal
#Bash

#una vez la secuencia NGS por curar se encuentre descargado en una carpeta quality, ejecutar: 

zcat "R1.fastq.gz " | head --> para identificar el formato 
zcat "R1.fastq.gz " | grep -c "@SRR" --> para buscar el numero de líneas que empiezan con dicho índice

#el uso de "zcat" es importante poque no queremos descomprimir todo el archivo y ocupar memoria

1)Uso del Fastqc para analizar el estado de las secuencias 

Fastqc R1.fastq.gz 
Fastqc R2.fastq.gz --> Se generarán archivos .html (revisar en resultados: R1_1er_QC)

2)Uso de trimmomatic: esto para eliminar las secuencias de baja calidad y eliminar adaptadores.

#Para eliminar sec de baja calidad: 
trimmomatic PE -threads 2 R1.fastq.gz R2.fastq.gz R1.PAIRED.fastq.gz R1.UNPAIRED.fastq.gz R2.PAIRED.fastq.gz R2.UNPAIRED.fastq.gz SLIDINGWINDOW:4:20

  Archivos input: R1.fasta.gz y R2.fasta.gz
  Archivos output: .PAIRED --> #estos archivos (PAIRED.html) tendran las secuencias curadas, con un phred >= 20







