<div align="center">
  <h2> 🌊️ AM-Modulation</h2>
</div>
<br/>

O objetivo desse projeto é a transmissão de um áudio que ocupe bandas de baixas frequências (entre 20 Hz e 2.500 Hz) através de um canal de transmissão em que você possa utilizar apenas as bandas entre 10.500 Hz e 15.500 Hz. 

Após a transmissão via sinal acústico, o receptor, que gravou o sinal transmitido, deverá demodular o sinal e reproduzi-lo, de maneira audível novamente.

--- 

<h4> 📝️ Etapas do projeto </h4>

---

<h5> 🔊️ Modularização do audio </h5>

- Leitura de um arquivo de áudio .wav de poucos segundos (entre 2 e 5) previamente gravado com uma
taxa de amostragem de **44100 Hz** (arquivo `audio/encoder/audio5s.wav`).

- Filtre e elimine as frequências acima de **2500 Hz**.

- Module esse sinal de áudio em AM com portadora de **13.000 Hz**. 

- Normalização do sinal de áudio.

<h5> 🎤️ Demodulação do audio </h5>

- Execute o áudio em um computador (`encoder.py`) e grave em outro (`decoder.py`), ou em caso de muito ruído, leia o arquivo de audio modularizado (arquivo `audio/encoder/audioModNorma.wav`) e peça para que seu colega grave o áudio modulado.

- Demodulação do audio recebido.

- Filtre as frequencias superiores **2.500Hz**.

---

<h4> ⚡️ Rodagem do código </h4>

---

Baixe as depêndencias necessárias para o funcionamento do código, copiando e colando no terminal o comando abaixo.

```bash

pip install -r requirements.txt

```
Escolha um computador será o Reprodutor de som da aplicação (`encoder.py`). Dessa forma, digite em seu terminal o comando:

```bash

python encoder.py

```


O outro computador para ser o receptor do audio e será repsonsável pela sua demodulação (`decoder.py`) , e rode em seu terminal o comando a seguir:

```bash

python Decoder.py

```


No prompt de comando surgirar um display de opções da ação que se deseja realizar, selecione uma das opções para a transmissao do som e tente sincronizar a reprodução final do áudio com a captação do mesmo pelo computador receptor.

👨‍💻️ Teste todas as possibilidades de som do display e divirta-se !  
