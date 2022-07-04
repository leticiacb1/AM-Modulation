<div align="center">
  <h2> 🌊️ AM-Modulation</h2>
</div>
<br/>

O objetivo desse projeto é a transmissão de um áudio que ocupe bandas de baixas frequências (entre 20 Hz e 2.500 Hz) através de um canal de transmissão em que você possa utilizar apenas as bandas entre 10.500 Hz e 15.500 Hz. 

Após a transmissão via sinal acústico, o receptor, que gravou o sinal transmitido, deverá demodular o sinal e reproduzi-lo, de maneira audível novamente.

<h4> 📝️ Etapas do projeto </h4>

<h5> 🔊️ Modularização do audio </h5>

- Leitura de um arquivo de áudio .wav de poucos segundos (entre 2 e 5) previamente gravado com uma
taxa de amostragem de **44100 Hz**.

- Filtre e elimine as frequências acima de **2500 Hz**.

- Module esse sinal de áudio em AM com portadora de **13.000 Hz**. 

- Normalização do sinal de áudio.

<h5> 🎤️ Demodulação do audio </h5>
