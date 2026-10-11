#Workflow: terminal
#Bash

#una vez la secuencia NGS por curar se encuentre descargado en una carpeta quality, ejecutar: 

zcat "R1.fastq.gz " | head --> para identificar el formato 
zcat "R1.fastq.gz " | grep -c "@SRR" --> para buscar el numero de líneas que empiezan con dicho índice

#el uso de "zcat" es importante poque no queremos descomprimir todo el archivo y ocupar memoria

1)Uso del Fastqc para analizar el estado de las secuencias 

Fastqc R1.fastq.gz 
Fastqc R2.fastq.gz --> Se generarán archivos .html (revisar en resultados: )
