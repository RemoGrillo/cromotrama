from bs4 import BeautifulSoup
import json

html_content = '''
<table class="wikitable sortable jquery-tablesorter" style="text-align:right;">

<thead><tr style="text-align:center;" bgcolor="#efefef">
<th rowspan="2" style="text-align:left" class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente">Nome
</th>
<th rowspan="2" width="60px" class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente">Esempio
</th>
<th rowspan="2" class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente">Esadecimale
</th>
<th colspan="3" style="border-left-width:thin"><a href="/wiki/RGB" title="RGB">RGB</a>
</th>
<th colspan="4" style="border-left-width:thin"><a href="/wiki/CMYK" title="CMYK">CMYK</a>
</th>
<th colspan="3" style="border-left-width:thin"><a href="/wiki/Hue_Saturation_Brightness" title="Hue Saturation Brightness">HSV</a>
</th></tr><tr>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Rosso" title="Rosso">R</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Verde" title="Verde">G</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Blu" title="Blu">B</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Ciano" title="Ciano">C</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Magenta_(colore)" title="Magenta (colore)">M</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Giallo" title="Giallo">Y</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente">K
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Tonalit%C3%A0_(colore)" class="mw-redirect" title="Tonalità (colore)">H</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Saturazione_cromatica" class="mw-redirect" title="Saturazione cromatica">S</a>
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Ordinamento crescente"><a href="/wiki/Luminosit%C3%A0_(percezione)" title="Luminosità (percezione)">B</a>
</th></tr></thead><tbody>

<tr>
<th style="text-align:left;"><span id="A"></span> <a href="/wiki/Acquamarina_(colore)" title="Acquamarina (colore)">Acquamarina</a>
</th>
<td style="background-color:#7fffd4;">
</td>
<td style="font-family:monospace;">#7FFFD4
</td>
<td style="border-left-width:thin;">127</td>
<td>255</td>
<td>212
</td>
<td style="border-left-width:thin;">50</td>
<td>0</td>
<td>17</td>
<td>0
</td>
<td style="border-left-width:thin;">159.8</td>
<td>50.2</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Albicocca_(colore)" class="mw-redirect" title="Albicocca (colore)">Albicocca</a>
</th>
<td style="background-color:#fbceb1;">
</td>
<td style="font-family:monospace;">#FBCEB1
</td>
<td style="border-left-width:thin;">251</td>
<td>206</td>
<td>177
</td>
<td style="border-left-width:thin;">0</td>
<td>18</td>
<td>29</td>
<td>2
</td>
<td style="border-left-width:thin;">24</td>
<td>29</td>
<td>98
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Amaranto_(colore)" title="Amaranto (colore)">Amaranto</a>
</th>
<td style="background-color:#E52B50;">
</td>
<td style="font-family:monospace;">#E52B50
</td>
<td style="border-left-width:thin;">229</td>
<td>43</td>
<td>80
</td>
<td style="border-left-width:thin;">0</td>
<td>81</td>
<td>65</td>
<td>10
</td>
<td style="border-left-width:thin;">348.1</td>
<td>81.2</td>
<td>89.8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Ambra_(colore)" title="Ambra (colore)">Ambra</a>
</th>
<td style="background-color:#FFBF00;">
</td>
<td style="font-family:monospace;">#FFBF00
</td>
<td style="border-left-width:thin;">255</td>
<td>191</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>25</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">44.9</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Ametista_(colore)" title="Ametista (colore)">Ametista</a>
</th>
<td style="background-color:#884DA7;">
</td>
<td style="font-family:monospace;">#884DA7
</td>
<td style="border-left-width:thin;">136</td>
<td>77</td>
<td>167
</td>
<td style="border-left-width:thin;">19</td>
<td>54</td>
<td>0</td>
<td>35
</td>
<td style="border-left-width:thin;">279</td>
<td>54</td>
<td>65
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Anguria_(colore)" title="Anguria (colore)">Anguria</a>
</th>
<td style="background-color:#fc6c85;">
</td>
<td style="font-family:monospace;">#FC6C85
</td>
<td style="border-left-width:thin;">252</td>
<td>108</td>
<td>133
</td>
<td style="border-left-width:thin;">0</td>
<td>57</td>
<td>47</td>
<td>1
</td>
<td style="border-left-width:thin;">350</td>
<td>57</td>
<td>99
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Antracite_(colore)" title="Antracite (colore)">Antracite</a>
</th>
<td style="background-color:#293133;">
</td>
<td style="font-family:monospace;">#293133
</td>
<td style="border-left-width:thin;">41</td>
<td>49</td>
<td>51
</td>
<td style="border-left-width:thin;">20</td>
<td>4</td>
<td>0</td>
<td>80
</td>
<td style="border-left-width:thin;">192</td>
<td>19.6</td>
<td>20
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Aragosta_(colore)" class="mw-redirect" title="Aragosta (colore)">Aragosta</a>
</th>
<td style="background-color:#ed7465;">
</td>
<td style="font-family:monospace;">#ED7465
</td>
<td style="border-left-width:thin;">237</td>
<td>116</td>
<td>101
</td>
<td style="border-left-width:thin;">0</td>
<td>51</td>
<td>57</td>
<td>7
</td>
<td style="border-left-width:thin;">7</td>
<td>57</td>
<td>93
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Arancione" title="Arancione">Arancione</a>
</th>
<td style="background-color:#FF6600;">
</td>
<td style="font-family:monospace;">#FF6600
</td>
<td style="border-left-width:thin;">255</td>
<td>102</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>60</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">24</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Ardesia_(colore)" title="Ardesia (colore)">Ardesia</a>
</th>
<td style="background-color:#708090;">
</td>
<td style="font-family:monospace;">#708090
</td>
<td style="border-left-width:thin;">112</td>
<td>128</td>
<td>144
</td>
<td style="border-left-width:thin;">22</td>
<td>11</td>
<td>0</td>
<td>44
</td>
<td style="border-left-width:thin;">210</td>
<td>22</td>
<td>56
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Argento_(colore)" title="Argento (colore)">Argento</a>
</th>
<td style="background-color:#C0C0C0;">
</td>
<td style="font-family:monospace;">#C0C0C0
</td>
<td style="border-left-width:thin;">192</td>
<td>192</td>
<td>192
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>25
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>75
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Asparago_(colore)" title="Asparago (colore)">Asparago</a>
</th>
<td style="background-color:#87a96b;">
</td>
<td style="font-family:monospace;">#87A96B
</td>
<td style="border-left-width:thin;">135</td>
<td>169</td>
<td>107
</td>
<td style="border-left-width:thin;">20</td>
<td>0</td>
<td>37</td>
<td>34
</td>
<td style="border-left-width:thin;">93</td>
<td>37</td>
<td>66
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Avio_(colore)" class="mw-redirect" title="Avio (colore)">Avio</a>
</th>
<td style="background-color:#5D8AA8;">
</td>
<td style="font-family:monospace;">#5D8AA8
</td>
<td style="border-left-width:thin;">93</td>
<td>138</td>
<td>168
</td>
<td style="border-left-width:thin;">45</td>
<td>18</td>
<td>0</td>
<td>34
</td>
<td style="border-left-width:thin;">204</td>
<td>44.6</td>
<td>65.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Avorio_(colore)" title="Avorio (colore)">Avorio</a>
</th>
<td style="background-color:#FFFFF0;">
</td>
<td style="font-family:monospace;">#FFFFF0
</td>
<td style="border-left-width:thin;">255</td>
<td>255</td>
<td>240
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>9</td>
<td>0
</td>
<td style="border-left-width:thin;">60</td>
<td>5.9</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Azalea_(colore)" title="Azalea (colore)">Azalea</a>
</th>
<td style="background-color:#d3305d;">
</td>
<td style="font-family:monospace;">#D3305D
</td>
<td style="border-left-width:thin;">211</td>
<td>48</td>
<td>93
</td>
<td style="border-left-width:thin;">0</td>
<td>77</td>
<td>56</td>
<td>17
</td>
<td style="border-left-width:thin;">343</td>
<td>77</td>
<td>83
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Azzurro" title="Azzurro">Azzurro</a>
</th>
<td style="background-color:#007fff;">
</td>
<td style="font-family:monospace;">#007FFF
</td>
<td style="border-left-width:thin;">0</td>
<td>127</td>
<td>255
</td>
<td style="border-left-width:thin;">100</td>
<td>50</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">210.1</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Azzurro_fiordaliso" class="mw-redirect" title="Azzurro fiordaliso">Azzurro fiordaliso</a>
</th>
<td style="background-color:#ABCDEF;">
</td>
<td style="font-family:monospace;">#ABCDEF
</td>
<td style="border-left-width:thin;">171</td>
<td>205</td>
<td>239
</td>
<td style="border-left-width:thin;">28</td>
<td>14</td>
<td>0</td>
<td>6
</td>
<td style="border-left-width:thin;">210</td>
<td>28</td>
<td>94
</td></tr>
<tr>
<th style="text-align:left;"><span id="B"></span> <a href="/wiki/Beige" title="Beige">Beige</a>
</th>
<td style="background-color:#f5f5dc;">
</td>
<td style="font-family:monospace;">#F5F5DC
</td>
<td style="border-left-width:thin;">245</td>
<td>245</td>
<td>220
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>10</td>
<td>4
</td>
<td style="border-left-width:thin;">60</td>
<td>10</td>
<td>96
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Beige-oliva_chiaro" title="Beige-oliva chiaro">Beige-oliva chiaro</a>
</th>
<td style="background-color:#908435;">
</td>
<td style="font-family:monospace;">#908435
</td>
<td style="border-left-width:thin;">144</td>
<td>132</td>
<td>53
</td>
<td style="border-left-width:thin;">0</td>
<td>9</td>
<td>66</td>
<td>41
</td>
<td style="border-left-width:thin;">52</td>
<td>63</td>
<td>56
</td></tr>

<tr>
<th style="text-align:left;"><a href="/wiki/Beige_verdastro" title="Beige verdastro">Beige verdastro</a>
</th>
<td style="background-color: #BEBD7F;">
</td>
<td style="font-family:monospace;">#BEBD7F
</td>
<td style="border-left-width:thin;">190</td>
<td>189</td>
<td>127
</td>
<td style="border-left-width:thin;">0</td>
<td>1</td>
<td>33</td>
<td>25
</td>
<td style="border-left-width:thin;">59</td>
<td>33.2</td>
<td>74.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco" title="Bianco">Bianco</a>
</th>
<td style="background-color:#FFFFFF;">
</td>
<td style="font-family:monospace;">#FFFFFF
</td>
<td style="border-left-width:thin;">255</td>
<td>255</td>
<td>255
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_antico" title="Bianco antico">Bianco antico</a>
</th>
<td style="background-color:#FFFEEF;">
</td>
<td style="font-family:monospace;">#FFFEEF
</td>
<td style="border-left-width:thin;">250</td>
<td>235</td>
<td>215
</td>
<td style="border-left-width:thin;">0</td>
<td>6</td>
<td>14</td>
<td>2
</td>
<td style="border-left-width:thin;">34</td>
<td>14</td>
<td>98
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_anti-flash" title="Bianco anti-flash">Bianco anti-flash</a>
</th>
<td style="background-color:#F2F3F4;">
</td>
<td style="font-family:monospace;">#F2F3F4
</td>
<td style="border-left-width:thin;">242</td>
<td>243</td>
<td>244
</td>
<td style="border-left-width:thin;">1</td>
<td>0</td>
<td>0</td>
<td>4
</td>
<td style="border-left-width:thin;">210</td>
<td>0.8</td>
<td>95.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_di_titanio" title="Bianco di titanio">Bianco di titanio</a>
</th>
<td style="background-color:#FAEBD7;">
</td>
<td style="font-family:monospace;">#FAEBD7
</td>
<td style="border-left-width:thin;">255</td>
<td>254</td>
<td>239
</td>
<td style="border-left-width:thin;">0</td>
<td>0,4</td>
<td>6,3</td>
<td>0
</td>
<td style="border-left-width:thin;">56</td>
<td>6</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_di_zinco" title="Bianco di zinco">Bianco di zinco</a>
</th>
<td style="background-color:#FEFEE9;">
</td>
<td style="font-family:monospace;">#FEFEE9
</td>
<td style="border-left-width:thin;">254</td>
<td>254</td>
<td>233
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>8,3</td>
<td>0,4
</td>
<td style="border-left-width:thin;">60</td>
<td>8.3</td>
<td>99.6
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_fantasma" title="Bianco fantasma">Bianco fantasma</a>
</th>
<td style="background-color:#F8F8FF;">
</td>
<td style="font-family:monospace;">#F8F8FF
</td>
<td style="border-left-width:thin;">248</td>
<td>248</td>
<td>255
</td>
<td style="border-left-width:thin;">3</td>
<td>3</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">240</td>
<td>2.7</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_floreale" title="Bianco floreale">Bianco floreale</a>
</th>
<td style="background-color:#FFFAF0;">
</td>
<td style="font-family:monospace;">#FFFAF0
</td>
<td style="border-left-width:thin;">255</td>
<td>250</td>
<td>240
</td>
<td style="border-left-width:thin;">0</td>
<td>2</td>
<td>6</td>
<td>0
</td>
<td style="border-left-width:thin;">40</td>
<td>5.9</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_fumo" title="Bianco fumo">Bianco fumo</a>
</th>
<td style="background-color:#F5F5F5;">
</td>
<td style="font-family:monospace;">#F5F5F5
</td>
<td style="border-left-width:thin;">245</td>
<td>245</td>
<td>245
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>4
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>96.1
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bianco_Navajo" title="Bianco Navajo">Bianco Navajo</a>
</th>
<td style="background-color:#FFDEAD;">
</td>
<td style="font-family:monospace;">#FFDEAD
</td>
<td style="border-left-width:thin;">255</td>
<td>222</td>
<td>173
</td>
<td style="border-left-width:thin;">0</td>
<td>13</td>
<td>32</td>
<td>0
</td>
<td style="border-left-width:thin;">35.9</td>
<td>32.2</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Biscotto_(colore)" title="Biscotto (colore)">Biscotto</a>
</th>
<td style="background-color:#FFE4C4;">
</td>
<td style="font-family:monospace;">#FFE4C4
</td>
<td style="border-left-width:thin;">255</td>
<td>228</td>
<td>196
</td>
<td style="border-left-width:thin;">0</td>
<td>11</td>
<td>23</td>
<td>0
</td>
<td style="border-left-width:thin;">33</td>
<td>23</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bistro" title="Bistro">Bistro</a>
</th>
<td style="background-color:#3D2B1F;">
</td>
<td style="font-family:monospace;">#3D2B1F
</td>
<td style="border-left-width:thin;">61</td>
<td>43</td>
<td>31
</td>
<td style="border-left-width:thin;">0</td>
<td>30</td>
<td>49</td>
<td>76
</td>
<td style="border-left-width:thin;">24</td>
<td>49.2</td>
<td>23.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu" title="Blu">Blu</a>
</th>
<td style="background-color:#0000ff;">
</td>
<td style="font-family:monospace;">#0000FF
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>255
</td>
<td style="border-left-width:thin;">100</td>
<td>100</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">240</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_acciaio" class="mw-redirect" title="Blu acciaio">Blu acciaio</a>
</th>
<td style="background-color:#4682B4;">
</td>
<td style="font-family:monospace;">#4682B4
</td>
<td style="border-left-width:thin;">70</td>
<td>130</td>
<td>180
</td>
<td style="border-left-width:thin;">63</td>
<td>28</td>
<td>0</td>
<td>29
</td>
<td style="border-left-width:thin;">207</td>
<td>61</td>
<td>71
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_alice" class="mw-redirect" title="Blu alice">Blu alice</a>
</th>
<td style="background-color:#F0F8FF;">
</td>
<td style="font-family:monospace;">#F0F8FF
</td>
<td style="border-left-width:thin;">240</td>
<td>248</td>
<td>255
</td>
<td style="border-left-width:thin;">4</td>
<td>1</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">208</td>
<td>6</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_Bondi" class="mw-redirect" title="Blu Bondi">Blu Bondi</a>
</th>
<td style="background-color:#0095B6;">
</td>
<td style="font-family:monospace;">#0095B6
</td>
<td style="border-left-width:thin;">0</td>
<td>149</td>
<td>182
</td>
<td style="border-left-width:thin;">100</td>
<td>18</td>
<td>0</td>
<td>29
</td>
<td style="border-left-width:thin;">191</td>
<td>100</td>
<td>71
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_cadetto" class="mw-redirect" title="Blu cadetto">Blu cadetto</a>
</th>
<td style="background-color:#5F9EA0;">
</td>
<td style="font-family:monospace;">#5F9EA0
</td>
<td style="border-left-width:thin;">95</td>
<td>158</td>
<td>160
</td>
<td style="border-left-width:thin;">41</td>
<td>1</td>
<td>0</td>
<td>37
</td>
<td style="border-left-width:thin;">182</td>
<td>41</td>
<td>63
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_ceruleo" class="mw-redirect" title="Blu ceruleo">Blu ceruleo</a>
</th>
<td style="background-color:#2A52BE;">
</td>
<td style="font-family:monospace;">#2A52BE
</td>
<td style="border-left-width:thin;">42</td>
<td>82</td>
<td>190
</td>
<td style="border-left-width:thin;">78</td>
<td>57</td>
<td>0</td>
<td>25
</td>
<td style="border-left-width:thin;">224</td>
<td>78</td>
<td>75
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_comando_stellare" class="mw-redirect" title="Blu comando stellare">Blu comando stellare</a>
</th>
<td style="background-color:#007BB8;">
</td>
<td style="font-family:monospace;">#007BB8
</td>
<td style="border-left-width:thin;">0</td>
<td>123</td>
<td>184
</td>
<td style="border-left-width:thin;">100</td>
<td>33</td>
<td>0</td>
<td>28
</td>
<td style="border-left-width:thin;">200</td>
<td>100</td>
<td>72.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_di_Persia" title="Blu di Persia">Blu di Persia</a>
</th>
<td style="background-color:#1C39BB;">
</td>
<td style="font-family:monospace;">#1C39BB
</td>
<td style="border-left-width:thin;">28</td>
<td>57</td>
<td>187
</td>
<td style="border-left-width:thin;">100</td>
<td>100</td>
<td>21</td>
<td>11
</td>
<td style="border-left-width:thin;">229</td>
<td>85</td>
<td>73
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_di_Prussia" title="Blu di Prussia">Blu di Prussia</a>
</th>
<td style="background-color:#003153;">
</td>
<td style="font-family:monospace;">#003153
</td>
<td style="border-left-width:thin;">0</td>
<td>49</td>
<td>83
</td>
<td style="border-left-width:thin;">63</td>
<td>35</td>
<td>14</td>
<td>72
</td>
<td style="border-left-width:thin;">205</td>
<td>100</td>
<td>43
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_Dodger" class="mw-redirect" title="Blu Dodger">Blu Dodger</a>
</th>
<td style="background-color:#1e90ff;">
</td>
<td style="font-family:monospace;">#1E90FF
</td>
<td style="border-left-width:thin;">30</td>
<td>144</td>
<td>255
</td>
<td style="border-left-width:thin;">88</td>
<td>44</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">210</td>
<td>88</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_elettrico" title="Blu elettrico">Blu elettrico</a>
</th>
<td style="background-color:#003399;">
</td>
<td style="font-family:monospace;">#003399
</td>
<td style="border-left-width:thin;">0</td>
<td>51</td>
<td>153
</td>
<td style="border-left-width:thin;">100</td>
<td>67</td>
<td>0</td>
<td>40
</td>
<td style="border-left-width:thin;">220</td>
<td>100</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_marino" title="Blu marino">Blu marino</a>
</th>
<td style="background-color:#000080;">
</td>
<td style="font-family:monospace;">#000080
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>128
</td>
<td style="border-left-width:thin;">100</td>
<td>100</td>
<td>0</td>
<td>50
</td>
<td style="border-left-width:thin;">240</td>
<td>100</td>
<td>50
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_scuro" class="mw-redirect" title="Blu scuro">Blu medio</a>
</th>
<td style="background-color:#0000CD;">
</td>
<td style="font-family:monospace;">#0000CD
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>205
</td>
<td style="border-left-width:thin;">100</td>
<td>100</td>
<td>0</td>
<td>20
</td>
<td style="border-left-width:thin;">240</td>
<td>100</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_notte_(colore)" class="mw-redirect" title="Blu notte (colore)">Blu notte</a>
</th>
<td style="background-color:#191970;">
</td>
<td style="font-family:monospace;">#191970
</td>
<td style="border-left-width:thin;">25</td>
<td>25</td>
<td>112
</td>
<td style="border-left-width:thin;">97</td>
<td>78</td>
<td>39</td>
<td>29
</td>
<td style="border-left-width:thin;">240</td>
<td>78</td>
<td>34
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_oltremare" title="Blu oltremare">Blu oltremare</a>
</th>
<td style="background-color:#120A8F;">
</td>
<td style="font-family:monospace;">#120A8F
</td>
<td style="border-left-width:thin;">18</td>
<td>10</td>
<td>143
</td>
<td style="border-left-width:thin;">100</td>
<td>90</td>
<td>4</td>
<td>1
</td>
<td style="border-left-width:thin;">244</td>
<td>93</td>
<td>56
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_polvere" class="mw-redirect" title="Blu polvere">Blu polvere</a>
</th>
<td style="background-color:#B0E0E6;">
</td>
<td style="font-family:monospace;">#B0E0E6
</td>
<td style="border-left-width:thin;">176</td>
<td>224</td>
<td>230
</td>
<td style="border-left-width:thin;">23</td>
<td>3</td>
<td>0</td>
<td>10
</td>
<td style="border-left-width:thin;">187</td>
<td>23</td>
<td>90
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_polvere_scuro" class="mw-redirect" title="Blu polvere scuro">Blu polvere scuro</a>
</th>
<td style="background-color:#003399;">
</td>
<td style="font-family:monospace;">#003399
</td>
<td style="border-left-width:thin;">0</td>
<td>51</td>
<td>153
</td>
<td style="border-left-width:thin;">100</td>
<td>67</td>
<td>0</td>
<td>40
</td>
<td style="border-left-width:thin;">220</td>
<td>100</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_reale" title="Blu reale">Blu reale</a>
</th>
<td style="background-color:#4169E1;">
</td>
<td style="font-family:monospace;">#4169E1
</td>
<td style="border-left-width:thin;">65</td>
<td>105</td>
<td>225
</td>
<td style="border-left-width:thin;">71</td>
<td>53</td>
<td>0</td>
<td>12
</td>
<td style="border-left-width:thin;">225</td>
<td>71</td>
<td>88
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Blu_scuro" class="mw-redirect" title="Blu scuro">Blu scuro</a>
</th>
<td style="background-color:#00008B;">
</td>
<td style="font-family:monospace;">#00008B
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>139
</td>
<td style="border-left-width:thin;">100</td>
<td>100</td>
<td>0</td>
<td>40
</td>
<td style="border-left-width:thin;">240</td>
<td>100</td>
<td>55
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bordeaux_(colore)" title="Bordeaux (colore)">Bordeaux</a>
</th>
<td style="background-color:#800000;">
</td>
<td style="font-family:monospace;">#800000
</td>
<td style="border-left-width:thin;">128</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>100</td>
<td>50
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>50
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Borgogna_(colore)" title="Borgogna (colore)">Borgogna</a>
</th>
<td style="background-color:#800020;">
</td>
<td style="font-family:monospace;">#800020
</td>
<td style="border-left-width:thin;">128</td>
<td>0</td>
<td>32
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>75</td>
<td>50
</td>
<td style="border-left-width:thin;">345</td>
<td>100</td>
<td>50.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bronzo_(colore)" title="Bronzo (colore)">Bronzo</a>
</th>
<td style="background-color:#CD7F32;">
</td>
<td style="font-family:monospace;">#CD7F32
</td>
<td style="border-left-width:thin;">205</td>
<td>127</td>
<td>50
</td>
<td style="border-left-width:thin;">0</td>
<td>38</td>
<td>76</td>
<td>20
</td>
<td style="border-left-width:thin;">29.8</td>
<td>75.6</td>
<td>80.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Bronzo_(colore)" title="Bronzo (colore)">Bronzo antico</a>
</th>
<td style="background-color:#75663F;">
</td>
<td style="font-family:monospace;">#75663F
</td>
<td style="border-left-width:thin;">117</td>
<td>102</td>
<td>63
</td>
<td style="border-left-width:thin;">0</td>
<td>13</td>
<td>46</td>
<td>54
</td>
<td style="border-left-width:thin;">43.3</td>
<td>46.2</td>
<td>45.9
</td></tr>
<tr>
<th style="text-align:left;"><span id="C"></span> <a href="/wiki/Camoscio_(colore)" title="Camoscio (colore)">Camoscio</a>
</th>
<td style="background-color:#F0DC82;">
</td>
<td style="font-family:monospace;">#F0DC82
</td>
<td style="border-left-width:thin;">240</td>
<td>220</td>
<td>130
</td>
<td style="border-left-width:thin;">0</td>
<td>8</td>
<td>46</td>
<td>6
</td>
<td style="border-left-width:thin;">49</td>
<td>46</td>
<td>94
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Carbone" title="Carbone">Carbone</a>
</th>
<td style="background-color:#050402;">
</td>
<td style="font-family:monospace;">#050402
</td>
<td style="border-left-width:thin;">5</td>
<td>4</td>
<td>2
</td>
<td style="border-left-width:thin;">0</td>
<td>20</td>
<td>60</td>
<td>98
</td>
<td style="border-left-width:thin;">40</td>
<td>60</td>
<td>2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Cardo_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Cardo (colore) (la pagina non esiste)">Cardo</a>
</th>
<td style="background-color:#D8BFD8;">
</td>
<td style="font-family:monospace;">#D8BFD8
</td>
<td style="border-left-width:thin;">216</td>
<td>191</td>
<td>216
</td>
<td style="border-left-width:thin;">0</td>
<td>12</td>
<td>0</td>
<td>15
</td>
<td style="border-left-width:thin;">300</td>
<td>11.6</td>
<td>84.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Carminio" title="Carminio">Carminio</a>
</th>
<td style="background-color:#960018;">
</td>
<td style="font-family:monospace;">#960018
</td>
<td style="border-left-width:thin;">150</td>
<td>0</td>
<td>24
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>84</td>
<td>41
</td>
<td style="border-left-width:thin;">350</td>
<td>100</td>
<td>59
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Carta_da_zucchero_(colore)" title="Carta da zucchero (colore)">Carta da zucchero</a>
</th>
<td style="background-color:#e0ffff;">
</td>
<td style="font-family:monospace;">#E0FFFF
</td>
<td style="border-left-width:thin;">224</td>
<td>255</td>
<td>255
</td>
<td style="border-left-width:thin;">12</td>
<td>0</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">180</td>
<td>12</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Castagno_(colore)" title="Castagno (colore)">Castagno</a>
</th>
<td style="background-color:#CD5C5C;">
</td>
<td style="font-family:monospace;">#CD5C5C
</td>
<td style="border-left-width:thin;">205</td>
<td>92</td>
<td>92
</td>
<td style="border-left-width:thin;">0</td>
<td>55</td>
<td>55</td>
<td>20
</td>
<td style="border-left-width:thin;">0</td>
<td>55.1</td>
<td>80.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Castagno_scuro" class="mw-redirect" title="Castagno scuro">Castagno scuro</a>
</th>
<td style="background-color:#986960;">
</td>
<td style="font-family:monospace;">#986960
</td>
<td style="border-left-width:thin;">152</td>
<td>105</td>
<td>96
</td>
<td style="border-left-width:thin;">0</td>
<td>32</td>
<td>36</td>
<td>38
</td>
<td style="border-left-width:thin;">10</td>
<td>37</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Castagno_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Castagno chiaro (la pagina non esiste)">Castagno chiaro</a>
</th>
<td style="background-color:#DDADAF;">
</td>
<td style="font-family:monospace;">#DDADAF
</td>
<td style="border-left-width:thin;">221</td>
<td>173</td>
<td>175
</td>
<td style="border-left-width:thin;">0</td>
<td>22</td>
<td>21</td>
<td>13
</td>
<td style="border-left-width:thin;">357</td>
<td>22</td>
<td>87
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Catrame_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Catrame (colore) (la pagina non esiste)">Catrame</a>
</th>
<td style="background-color:#D2B48C;">
</td>
<td style="font-family:monospace;">#D2B48C
</td>
<td style="border-left-width:thin;">210</td>
<td>180</td>
<td>140
</td>
<td style="border-left-width:thin;">0</td>
<td>14</td>
<td>33</td>
<td>18
</td>
<td style="border-left-width:thin;">34</td>
<td>33</td>
<td>82
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Catrame_scuro&amp;action=edit&amp;redlink=1" class="new" title="Catrame scuro (la pagina non esiste)">Catrame scuro</a>
</th>
<td style="background-color:#918151;">
</td>
<td style="font-family:monospace;">#918151
</td>
<td style="border-left-width:thin;">145</td>
<td>129</td>
<td>81
</td>
<td style="border-left-width:thin;">0</td>
<td>12</td>
<td>44</td>
<td>41
</td>
<td style="border-left-width:thin;">45</td>
<td>44</td>
<td>57
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Celadon_(colore)" title="Celadon (colore)">Celadon</a>
</th>
<td style="background-color:#ACE1AF;">
</td>
<td style="font-family:monospace;">#ACE1AF
</td>
<td style="border-left-width:thin;">172</td>
<td>225</td>
<td>175
</td>
<td style="border-left-width:thin;">21</td>
<td>0</td>
<td>19</td>
<td>12
</td>
<td style="border-left-width:thin;">123</td>
<td>24</td>
<td>88
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Celeste_(colore)" title="Celeste (colore)">Celeste</a>
</th>
<td style="background-color:#99CBFF;">
</td>
<td style="font-family:monospace;">#99CBFF
</td>
<td style="border-left-width:thin;">153</td>
<td>203</td>
<td>255
</td>
<td style="border-left-width:thin;">43</td>
<td>13</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">211</td>
<td>40</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Ceruleo" title="Ceruleo">Ceruleo</a>
</th>
<td style="background-color:#007BA7;">
</td>
<td style="font-family:monospace;">#007BA7
</td>
<td style="border-left-width:thin;">0</td>
<td>123</td>
<td>167
</td>
<td style="border-left-width:thin;">100</td>
<td>26</td>
<td>0</td>
<td>35
</td>
<td style="border-left-width:thin;">196</td>
<td>100</td>
<td>65
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Ceruleo_scuro&amp;action=edit&amp;redlink=1" class="new" title="Ceruleo scuro (la pagina non esiste)">Ceruleo scuro</a>
</th>
<td style="background-color:#08457E;">
</td>
<td style="font-family:monospace;">#08457E
</td>
<td style="border-left-width:thin;">8</td>
<td>69</td>
<td>126
</td>
<td style="border-left-width:thin;">93</td>
<td>43</td>
<td>0</td>
<td>51
</td>
<td style="border-left-width:thin;">209</td>
<td>94</td>
<td>49
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Chartreuse_(colore)" title="Chartreuse (colore)">Chartreuse</a>
</th>
<td style="background-color:#7fff00;">
</td>
<td style="font-family:monospace;">#7FFF00
</td>
<td style="border-left-width:thin;">127</td>
<td>255</td>
<td>0
</td>
<td style="border-left-width:thin;">50</td>
<td>0</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">90.1</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Ciano" title="Ciano">Ciano</a>
</th>
<td style="background-color:#00ffff;">
</td>
<td style="font-family:monospace;">#00FFFF
</td>
<td style="border-left-width:thin;">0</td>
<td>255</td>
<td>255
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">180</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Ciliegia_(colore)" title="Ciliegia (colore)">Ciliegia</a>
</th>
<td style="background-color:#DE3163;">
</td>
<td style="font-family:monospace;">#DE3163
</td>
<td style="border-left-width:thin;">194</td>
<td>0</td>
<td>50
</td>
<td style="border-left-width:thin;">0</td>
<td>78</td>
<td>55</td>
<td>13
</td>
<td style="border-left-width:thin;">343</td>
<td>78</td>
<td>87
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Cioccolato_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Cioccolato (colore) (la pagina non esiste)">Cioccolato</a>
</th>
<td style="background-color:#D2691E;">
</td>
<td style="font-family:monospace;">#D2691E
</td>
<td style="border-left-width:thin;">210</td>
<td>105</td>
<td>30
</td>
<td style="border-left-width:thin;">0</td>
<td>50</td>
<td>86</td>
<td>18
</td>
<td style="border-left-width:thin;">25</td>
<td>86</td>
<td>82
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Cobalto_(colore)" title="Cobalto (colore)">Cobalto</a>
</th>
<td style="background-color:#0047AB;">
</td>
<td style="font-family:monospace;">#0047AB
</td>
<td style="border-left-width:thin;">0</td>
<td>71</td>
<td>171
</td>
<td style="border-left-width:thin;">100</td>
<td>58</td>
<td>0</td>
<td>33
</td>
<td style="border-left-width:thin;">215</td>
<td>100</td>
<td>67
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Conchiglia_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Conchiglia (colore) (la pagina non esiste)">Conchiglia</a>
</th>
<td style="background-color:#FFF5EE;">
</td>
<td style="font-family:monospace;">#FFF5EE
</td>
<td style="border-left-width:thin;">255</td>
<td>245</td>
<td>238
</td>
<td style="border-left-width:thin;">0</td>
<td>3</td>
<td>6</td>
<td>0
</td>
<td style="border-left-width:thin;">25</td>
<td>7</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Corallo_(colore)" title="Corallo (colore)">Corallo</a>
</th>
<td style="background-color:#ff7f50;">
</td>
<td style="font-family:monospace;">#FF7F50
</td>
<td style="border-left-width:thin;">255</td>
<td>127</td>
<td>80
</td>
<td style="border-left-width:thin;">0</td>
<td>50</td>
<td>69</td>
<td>0
</td>
<td style="border-left-width:thin;">16</td>
<td>69</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Crema_(colore)" title="Crema (colore)">Crema</a>
</th>
<td style="background-color:#FFFDD0;">
</td>
<td style="font-family:monospace;">#FFFDD0
</td>
<td style="border-left-width:thin;">255</td>
<td>253</td>
<td>208
</td>
<td style="border-left-width:thin;">0</td>
<td>1</td>
<td>18</td>
<td>0
</td>
<td style="border-left-width:thin;">57</td>
<td>18</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Cremisi" title="Cremisi">Cremisi</a>
</th>
<td style="background-color:#dc143c;">
</td>
<td style="font-family:monospace;">#DC143C
</td>
<td style="border-left-width:thin;">220</td>
<td>20</td>
<td>60
</td>
<td style="border-left-width:thin;">0</td>
<td>91</td>
<td>73</td>
<td>14
</td>
<td style="border-left-width:thin;">348</td>
<td>91</td>
<td>86
</td></tr>
<tr>
<th style="text-align:left;"><span id="D"></span> <a href="/wiki/Denim_(colore)" title="Denim (colore)">Denim</a>
</th>
<td style="background-color:#1560BD;">
</td>
<td style="font-family:monospace;">#1560BD
</td>
<td style="border-left-width:thin;">21</td>
<td>96</td>
<td>189
</td>
<td style="border-left-width:thin;">89</td>
<td>49</td>
<td>0</td>
<td>26
</td>
<td style="border-left-width:thin;">213</td>
<td>89</td>
<td>74
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Denim_chiaro" class="mw-redirect" title="Denim chiaro">Denim chiaro</a>
</th>
<td style="background-color:#5E86C1;">
</td>
<td style="font-family:monospace;">#5E86C1
</td>
<td style="border-left-width:thin;">94</td>
<td>134</td>
<td>193
</td>
<td style="border-left-width:thin;">51</td>
<td>31</td>
<td>0</td>
<td>24
</td>
<td style="border-left-width:thin;">216</td>
<td>51</td>
<td>76
</td></tr>
<tr>
<th style="text-align:left;"><span id="E"></span> <a href="/wiki/Eliotropo" title="Eliotropo">Eliotropo</a>
</th>
<td style="background-color:#DF73FF;">
</td>
<td style="font-family:monospace;">#DF73FF
</td>
<td style="border-left-width:thin;">223</td>
<td>115</td>
<td>255
</td>
<td style="border-left-width:thin;">13</td>
<td>55</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">286</td>
<td>55</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/%C3%89cru" title="Écru">Écru</a>
</th>
<td style="background-color:#C2B280;">
</td>
<td style="font-family:monospace;">#C2B280
</td>
<td style="border-left-width:thin;">194</td>
<td>178</td>
<td>128
</td>
<td style="border-left-width:thin;">0</td>
<td>8</td>
<td>34</td>
<td>24
</td>
<td style="border-left-width:thin;">45</td>
<td>34</td>
<td>76
</td></tr>
<tr>
<th style="text-align:left;"><span id="F"></span> <a href="/wiki/Blu_fiore_di_granturco" class="mw-redirect" title="Blu fiore di granturco">Fiore di granturco</a>
</th>
<td style="background-color:#6495ED;">
</td>
<td style="font-family:monospace;">#6495ED
</td>
<td style="border-left-width:thin;">100</td>
<td>149</td>
<td>237
</td>
<td style="border-left-width:thin;">58</td>
<td>37</td>
<td>0</td>
<td>7
</td>
<td style="border-left-width:thin;">219</td>
<td>58</td>
<td>93
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Foglia_di_t%C3%A8_(colore)" title="Foglia di tè (colore)">Foglia di tè</a>
</th>
<td style="background-color:#008080;">
</td>
<td style="font-family:monospace;">#008080
</td>
<td style="border-left-width:thin;">0</td>
<td>128</td>
<td>128
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>0</td>
<td>50
</td>
<td style="border-left-width:thin;">180</td>
<td>100</td>
<td>50
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Fucsia" title="Fucsia">Fucsia</a>
</th>
<td style="background-color:#f400a1;">
</td>
<td style="font-family:monospace;">#F400A1
</td>
<td style="border-left-width:thin;">244</td>
<td>0</td>
<td>161
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>34</td>
<td>4
</td>
<td style="border-left-width:thin;">320</td>
<td>100</td>
<td>96
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Fulvo" class="mw-redirect" title="Fulvo">Fulvo</a>
</th>
<td style="background-color:#EBB55F;">
</td>
<td style="font-family:monospace;">#EBB55F
</td>
<td style="border-left-width:thin;">235</td>
<td>181</td>
<td>95
</td>
<td style="border-left-width:thin;">0</td>
<td>23</td>
<td>60</td>
<td>8
</td>
<td style="border-left-width:thin;">36.9</td>
<td>59.6</td>
<td>92.2
</td></tr>
<tr>
<th style="text-align:left;"><span id="G"></span> <a href="/wiki/Gainsboro" title="Gainsboro">Gainsboro</a>
</th>
<td style="background-color:#DCDCDC;">
</td>
<td style="font-family:monospace;">#DCDCDC
</td>
<td style="border-left-width:thin;">220</td>
<td>220</td>
<td>220
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>14
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>86.3
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Giada_(colore)" title="Giada (colore)">Giada</a>
</th>
<td style="background-color:#00A86B;">
</td>
<td style="font-family:monospace;">#00A86B
</td>
<td style="border-left-width:thin;">0</td>
<td>168</td>
<td>107
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>36</td>
<td>34
</td>
<td style="border-left-width:thin;">158.2</td>
<td>100</td>
<td>65.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Giallo" title="Giallo">Giallo</a>
</th>
<td style="background-color:#FFFF00;">
</td>
<td style="font-family:monospace;">#FFFF00
</td>
<td style="border-left-width:thin;">255</td>
<td>255</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">60</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Giallo_miele&amp;action=edit&amp;redlink=1" class="new" title="Giallo miele (la pagina non esiste)">Giallo miele</a>
</th>
<td style="background-color:#A98307;">
</td>
<td style="font-family:monospace;">#A98307
</td>
<td style="border-left-width:thin;">169</td>
<td>131</td>
<td>7
</td>
<td style="border-left-width:thin;">0</td>
<td>22</td>
<td>96</td>
<td>34
</td>
<td style="border-left-width:thin;">45.9</td>
<td>95.9</td>
<td>66.3
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Giallo_Napoli" title="Giallo Napoli">Giallo Napoli</a>
</th>
<td style="background-color:#F7E89F;">
</td>
<td style="font-family:monospace;">#F7E89F
</td>
<td style="border-left-width:thin;">247</td>
<td>232</td>
<td>159
</td>
<td style="border-left-width:thin;">0</td>
<td>6</td>
<td>36</td>
<td>3
</td>
<td style="border-left-width:thin;">49.8</td>
<td>35.6</td>
<td>96.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Giallo_pastello" title="Giallo pastello">Giallo pastello</a>
</th>
<td style="background-color:#FFFF66;">
</td>
<td style="font-family:monospace;">#FFFF66
</td>
<td style="border-left-width:thin;">255</td>
<td>255</td>
<td>102
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>60</td>
<td>0
</td>
<td style="border-left-width:thin;">60</td>
<td>60</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Giallo_sabbia&amp;action=edit&amp;redlink=1" class="new" title="Giallo sabbia (la pagina non esiste)">Giallo sabbia</a>
</th>
<td style="background-color:#C6A664;">
</td>
<td style="font-family:monospace;">#C6A664
</td>
<td style="border-left-width:thin;">198</td>
<td>166</td>
<td>100
</td>
<td style="border-left-width:thin;">0</td>
<td>16</td>
<td>49</td>
<td>22
</td>
<td style="border-left-width:thin;">40.4</td>
<td>49.5</td>
<td>77.6
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Giallo_segnale&amp;action=edit&amp;redlink=1" class="new" title="Giallo segnale (la pagina non esiste)">Giallo segnale</a>
</th>
<td style="background-color:#E5BE01;">
</td>
<td style="font-family:monospace;">#E5BE01
</td>
<td style="border-left-width:thin;">229</td>
<td>190</td>
<td>1
</td>
<td style="border-left-width:thin;">0</td>
<td>17</td>
<td>100</td>
<td>10
</td>
<td style="border-left-width:thin;">49.7</td>
<td>99.6</td>
<td>89,8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Giallo_scuolabus" title="Giallo scuolabus">Giallo scuolabus</a>
</th>
<td style="background-color:#ffd800;">
</td>
<td style="font-family:monospace;">#FFD800
</td>
<td style="border-left-width:thin;">255</td>
<td>216</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>15</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">50.8</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Glicine_(colore)" title="Glicine (colore)">Glicine</a>
</th>
<td style="background-color:#C9A0DC;">
</td>
<td style="font-family:monospace;">#C9A0DC
</td>
<td style="border-left-width:thin;">201</td>
<td>160</td>
<td>220
</td>
<td style="border-left-width:thin;">9</td>
<td>27</td>
<td>0</td>
<td>14
</td>
<td style="border-left-width:thin;">281</td>
<td>27.3</td>
<td>86.3
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Granata_(colore)" title="Granata (colore)">Granata</a>
</th>
<td style="background-color:#7B1B02;">
</td>
<td style="font-family:monospace;">#7B1B02
</td>
<td style="border-left-width:thin;">123</td>
<td>27</td>
<td>2
</td>
<td style="border-left-width:thin;">0</td>
<td>78</td>
<td>98</td>
<td>52
</td>
<td style="border-left-width:thin;">12.4</td>
<td>98.4</td>
<td>48.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grano_(colore)" title="Grano (colore)">Grano</a>
</th>
<td style="background-color:#F5DEB3;">
</td>
<td style="font-family:monospace;">#F5DEB3
</td>
<td style="border-left-width:thin;">245</td>
<td>222</td>
<td>179
</td>
<td style="border-left-width:thin;">0</td>
<td>9</td>
<td>27</td>
<td>4
</td>
<td style="border-left-width:thin;">39.1</td>
<td>26.9</td>
<td>96.1
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_5%25" class="mw-redirect" title="Grigio 5%">Grigio 5%</a>
</th>
<td style="background-color:#F7F7F7;">
</td>
<td style="font-family:monospace;">#F7F7F7
</td>
<td style="border-left-width:thin;">247</td>
<td>247</td>
<td>247
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>3
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>96.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_10%25" class="mw-redirect" title="Grigio 10%">Grigio 10%</a>
</th>
<td style="background-color:#EFEFEF;">
</td>
<td style="font-family:monospace;">#EFEFEF
</td>
<td style="border-left-width:thin;">239</td>
<td>239</td>
<td>239
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>6
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>93.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_15%25" class="mw-redirect" title="Grigio 15%">Grigio 15%</a>
</th>
<td style="background-color:#E1E1E1;">
</td>
<td style="font-family:monospace;">#E1E1E1
</td>
<td style="border-left-width:thin;">225</td>
<td>225</td>
<td>225
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>15
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>?
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_20%25" class="mw-redirect" title="Grigio 20%">Grigio 20%</a>
</th>
<td style="background-color:#D2D2D2;">
</td>
<td style="font-family:monospace;">#D2D2D2
</td>
<td style="border-left-width:thin;">210</td>
<td>210</td>
<td>210
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>18
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>82.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_25%25" class="mw-redirect" title="Grigio 25%">Grigio 25%</a>
</th>
<td style="background-color:#C0C0C0;">
</td>
<td style="font-family:monospace;">#C0C0C0
</td>
<td style="border-left-width:thin;">192</td>
<td>192</td>
<td>192
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>25
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>?
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_30%25" class="mw-redirect" title="Grigio 30%">Grigio 30%</a>
</th>
<td style="background-color:#B2B2B2;">
</td>
<td style="font-family:monospace;">#B2B2B2
</td>
<td style="border-left-width:thin;">178</td>
<td>178</td>
<td>178
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>30
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>69.8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_35%25" class="mw-redirect" title="Grigio 35%">Grigio 35%</a>
</th>
<td style="background-color:#A2A2A2;">
</td>
<td style="font-family:monospace;">#A2A2A2
</td>
<td style="border-left-width:thin;">162</td>
<td>162</td>
<td>162
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>35
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>?
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_40%25" class="mw-redirect" title="Grigio 40%">Grigio 40%</a>
</th>
<td style="background-color:#8F8F8F;">
</td>
<td style="font-family:monospace;">#8F8F8F
</td>
<td style="border-left-width:thin;">147</td>
<td>147</td>
<td>147
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>44
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>56.1
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_50%25" class="mw-redirect" title="Grigio 50%">Grigio 50%</a>
</th>
<td style="background-color:#808080;">
</td>
<td style="font-family:monospace;">#808080
</td>
<td style="border-left-width:thin;">128</td>
<td>128</td>
<td>128
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>50
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>50.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_60%25" class="mw-redirect" title="Grigio 60%">Grigio 60%</a>
</th>
<td style="background-color:#5F5F5F;">
</td>
<td style="font-family:monospace;">#5F5F5F
</td>
<td style="border-left-width:thin;">95</td>
<td>95</td>
<td>95
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>63
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>37.3
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_70%25" class="mw-redirect" title="Grigio 70%">Grigio 70%</a>
</th>
<td style="background-color:#4F4F4F;">
</td>
<td style="font-family:monospace;">#4F4F4F
</td>
<td style="border-left-width:thin;">79</td>
<td>79</td>
<td>79
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>69
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>31
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_75%25" class="mw-redirect" title="Grigio 75%">Grigio 75%</a>
</th>
<td style="background-color:#404040;">
</td>
<td style="font-family:monospace;">#404040
</td>
<td style="border-left-width:thin;">64</td>
<td>64</td>
<td>64
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>75
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>25.1
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_80%25" class="mw-redirect" title="Grigio 80%">Grigio 80%</a>
</th>
<td style="background-color:#2F2F2F;">
</td>
<td style="font-family:monospace;">#2F2F2F
</td>
<td style="border-left-width:thin;">47</td>
<td>47</td>
<td>47
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>82
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>18.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_asparago" title="Grigio asparago">Grigio asparago</a>
</th>
<td style="background-color:#465945;">
</td>
<td style="font-family:monospace;">#465945
</td>
<td style="border-left-width:thin;">70</td>
<td>89</td>
<td>69
</td>
<td style="border-left-width:thin;">21</td>
<td>0</td>
<td>22</td>
<td>65
</td>
<td style="border-left-width:thin;">117</td>
<td>22.5</td>
<td>34.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_ardesia_scuro" class="mw-redirect" title="Grigio ardesia scuro">Grigio ardesia scuro</a>
</th>
<td style="background-color:#2F4F4F;">
</td>
<td style="font-family:monospace;">#2F4F4F
</td>
<td style="border-left-width:thin;">47</td>
<td>79</td>
<td>79
</td>
<td style="border-left-width:thin;">41</td>
<td>0</td>
<td>0</td>
<td>69
</td>
<td style="border-left-width:thin;">180</td>
<td>41</td>
<td>31
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_ardesia_chiaro" class="mw-redirect" title="Grigio ardesia chiaro">Grigio ardesia chiaro</a>
</th>
<td style="background-color:#778899;">
</td>
<td style="font-family:monospace;">#778899
</td>
<td style="border-left-width:thin;">119</td>
<td>136</td>
<td>153
</td>
<td style="border-left-width:thin;">60</td>
<td>43</td>
<td>34</td>
<td>4
</td>
<td style="border-left-width:thin;">210</td>
<td>22</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Grigio_cenere" title="Grigio cenere">Grigio cenere</a>
</th>
<td style="background-color:#E4E5E0;">
</td>
<td style="font-family:monospace;">#E4E5E0
</td>
<td style="border-left-width:thin;">228</td>
<td>229</td>
<td>224
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>2</td>
<td>10
</td>
<td style="border-left-width:thin;">72</td>
<td>2.2</td>
<td>89.8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Grigio_topo_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Grigio topo (colore) (la pagina non esiste)">Grigio topo</a>
</th>
<td style="background-color:#646B63;">
</td>
<td style="font-family:monospace;">#646B63
</td>
<td style="border-left-width:thin;">100</td>
<td>107</td>
<td>99
</td>
<td style="border-left-width:thin;">7</td>
<td>0</td>
<td>7</td>
<td>58
</td>
<td style="border-left-width:thin;">112.5</td>
<td>7.5</td>
<td>42
</td></tr>
<tr>
<th style="text-align:left;"><span id="I"></span> <a href="/wiki/Incarnato_prugna" title="Incarnato prugna">Incarnato prugna</a>
</th>
<td style="background-color:#CC8899;">
</td>
<td style="font-family:monospace;">#CC8899
</td>
<td style="border-left-width:thin;">204</td>
<td>136</td>
<td>153
</td>
<td style="border-left-width:thin;">0</td>
<td>33</td>
<td>25</td>
<td>20
</td>
<td style="border-left-width:thin;">345</td>
<td>33</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Indaco_(colore)" title="Indaco (colore)">Indaco</a>
</th>
<td style="background-color:#4B0082;">
</td>
<td style="font-family:monospace;">#4B0082
</td>
<td style="border-left-width:thin;">75</td>
<td>0</td>
<td>130
</td>
<td style="border-left-width:thin;">42</td>
<td>100</td>
<td>0</td>
<td>49
</td>
<td style="border-left-width:thin;">275</td>
<td>100</td>
<td>51
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Indaco_elettrico" class="mw-redirect" title="Indaco elettrico">Indaco elettrico</a>
</th>
<td style="background-color:#6F00FF;">
</td>
<td style="font-family:monospace;">#6F00FF
</td>
<td style="border-left-width:thin;">111</td>
<td>0</td>
<td>255
</td>
<td style="border-left-width:thin;">56</td>
<td>100</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">266.1</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Indaco_(colore)" title="Indaco (colore)">Indaco scuro</a>
</th>
<td style="background-color:#310062;">
</td>
<td style="font-family:monospace;">#310062
</td>
<td style="border-left-width:thin;">49</td>
<td>0</td>
<td>98
</td>
<td style="border-left-width:thin;">92</td>
<td>100</td>
<td>22</td>
<td>29
</td>
<td style="border-left-width:thin;">270</td>
<td>100</td>
<td>38
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/International_Klein_Blue" title="International Klein Blue">International Klein Blue</a>
</th>
<td style="background-color:#002FA7;">
</td>
<td style="font-family:monospace;">#002FA7
</td>
<td style="border-left-width:thin;">0</td>
<td>47</td>
<td>167
</td>
<td style="border-left-width:thin;">100</td>
<td>72</td>
<td>0</td>
<td>35
</td>
<td style="border-left-width:thin;">223.1</td>
<td>100</td>
<td>65.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Isabella_(colore)" title="Isabella (colore)">Isabella</a>
</th>
<td style="background-color:#F4F0EC;">
</td>
<td style="font-family:monospace;">#F4F0EC
</td>
<td style="border-left-width:thin;">244</td>
<td>240</td>
<td>236
</td>
<td style="border-left-width:thin;">0</td>
<td>2</td>
<td>3</td>
<td>4
</td>
<td style="border-left-width:thin;">30</td>
<td>3.3</td>
<td>95.7
</td></tr>
<tr>
<th style="text-align:left;"><span id="K"></span> <a href="/wiki/Cachi_(colore)" title="Cachi (colore)">Kaki</a>
</th>
<td style="background-color:#C3B091;">
</td>
<td style="font-family:monospace;">#C3B091
</td>
<td style="border-left-width:thin;">195</td>
<td>176</td>
<td>145
</td>
<td style="border-left-width:thin;">0</td>
<td>10</td>
<td>26</td>
<td>24
</td>
<td style="border-left-width:thin;">37</td>
<td>26</td>
<td>76
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Cachi_(colore)#Cachi_chiaro_o_catrame" title="Cachi (colore)">Kaki chiaro</a>
</th>
<td style="background-color:#F0E68C;">
</td>
<td style="font-family:monospace;">#F0E68C
</td>
<td style="border-left-width:thin;">240</td>
<td>230</td>
<td>140
</td>
<td style="border-left-width:thin;">0</td>
<td>4</td>
<td>42</td>
<td>6
</td>
<td style="border-left-width:thin;">56</td>
<td>43</td>
<td>74
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Cachi_(colore)#Cachi_scuro" title="Cachi (colore)">Kaki scuro</a>
</th>
<td style="background-color:#BDB76B;">
</td>
<td style="font-family:monospace;">#BDB76B
</td>
<td style="border-left-width:thin;">189</td>
<td>183</td>
<td>107
</td>
<td style="border-left-width:thin;">0</td>
<td>3</td>
<td>43</td>
<td>26
</td>
<td style="border-left-width:thin;">54</td>
<td>41</td>
<td>94
</td></tr>
<tr>
<th style="text-align:left;"><span id="L"></span> <a href="/w/index.php?title=Lampone_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Lampone (colore) (la pagina non esiste)">Lampone</a>
</th>
<td style="background-color:#E30B5C;">
</td>
<td style="font-family:monospace;">#E30B5C
</td>
<td style="border-left-width:thin;">227</td>
<td>11</td>
<td>92
</td>
<td style="border-left-width:thin;">0</td>
<td>95</td>
<td>59</td>
<td>11
</td>
<td style="border-left-width:thin;">337.5</td>
<td>95.2</td>
<td>89
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Lavanda_(colore)" title="Lavanda (colore)">Lavanda</a>
</th>
<td style="background-color:#E6E6FA;">
</td>
<td style="font-family:monospace;">#E6E6FA
</td>
<td style="border-left-width:thin;">230</td>
<td>230</td>
<td>250
</td>
<td style="border-left-width:thin;">8</td>
<td>8</td>
<td>0</td>
<td>2
</td>
<td style="border-left-width:thin;">240</td>
<td>8</td>
<td>98
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Lavanda_pallido&amp;action=edit&amp;redlink=1" class="new" title="Lavanda pallido (la pagina non esiste)">Lavanda pallido</a>
</th>
<td style="background-color:#DABAD0;">
</td>
<td style="font-family:monospace;">#DABAD0
</td>
<td style="border-left-width:thin;">218</td>
<td>186</td>
<td>208
</td>
<td style="border-left-width:thin;">0</td>
<td>15</td>
<td>5</td>
<td>15
</td>
<td style="border-left-width:thin;">318.8</td>
<td>14.7</td>
<td>85.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Lavanda_rosata" class="mw-redirect" title="Lavanda rosata">Lavanda rosata</a>
</th>
<td style="background-color:#FFF0F5;">
</td>
<td style="font-family:monospace;">#FFF0F5
</td>
<td style="border-left-width:thin;">255</td>
<td>240</td>
<td>245
</td>
<td style="border-left-width:thin;">0</td>
<td>6</td>
<td>4</td>
<td>0
</td>
<td style="border-left-width:thin;">340</td>
<td>5.9</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Limone_(colore)" title="Limone (colore)">Limone</a>
</th>
<td style="background-color:#FDE910;">
</td>
<td style="font-family:monospace;">#FDE910
</td>
<td style="border-left-width:thin;">253</td>
<td>233</td>
<td>16
</td>
<td style="border-left-width:thin;">0</td>
<td>8</td>
<td>94</td>
<td>1
</td>
<td style="border-left-width:thin;">55</td>
<td>94</td>
<td>99
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Limone_crema" title="Limone crema">Limone crema</a>
</th>
<td style="background-color:#FFFACD;">
</td>
<td style="font-family:monospace;">#FFFACD
</td>
<td style="border-left-width:thin;">255</td>
<td>250</td>
<td>205
</td>
<td style="border-left-width:thin;">0</td>
<td>2</td>
<td>20</td>
<td>0
</td>
<td style="border-left-width:thin;">54</td>
<td>20</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Lilla_(colore)" title="Lilla (colore)">Lilla</a>
</th>
<td style="background-color:#C8A2C8;">
</td>
<td style="font-family:monospace;">#C8A2C8
</td>
<td style="border-left-width:thin;">200</td>
<td>162</td>
<td>200
</td>
<td style="border-left-width:thin;">0</td>
<td>19</td>
<td>0</td>
<td>22
</td>
<td style="border-left-width:thin;">300</td>
<td>19</td>
<td>78
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Lime_(colore)" title="Lime (colore)">Lime</a>
</th>
<td style="background-color:#CCFF00;">
</td>
<td style="font-family:monospace;">#CCFF00
</td>
<td style="border-left-width:thin;">204</td>
<td>255</td>
<td>0
</td>
<td style="border-left-width:thin;">20</td>
<td>0</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">72</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Lino_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Lino (colore) (la pagina non esiste)">Lino</a>
</th>
<td style="background-color:#FAF0E6;">
</td>
<td style="font-family:monospace;">#FAF0E6
</td>
<td style="border-left-width:thin;">250</td>
<td>240</td>
<td>230
</td>
<td style="border-left-width:thin;">0</td>
<td>4</td>
<td>8</td>
<td>2
</td>
<td style="border-left-width:thin;">30</td>
<td>8</td>
<td>98
</td></tr>
<tr>
<th style="text-align:left;"><span id="M"></span> <a href="/wiki/Magenta_(colore)" title="Magenta (colore)">Magenta</a>
</th>
<td style="background-color:#FF00FF;">
</td>
<td style="font-family:monospace;">#FF00FF
</td>
<td style="border-left-width:thin;">255</td>
<td>0</td>
<td>255
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">300</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Magenta_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Magenta chiaro (la pagina non esiste)">Magenta chiaro</a>
</th>
<td style="background-color:#F984E5;">
</td>
<td style="font-family:monospace;">#F984E5
</td>
<td style="border-left-width:thin;">249</td>
<td>132</td>
<td>229
</td>
<td style="border-left-width:thin;">0</td>
<td>47</td>
<td>8</td>
<td>2
</td>
<td style="border-left-width:thin;">310.3</td>
<td>47</td>
<td>97.6
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Magnolia_(colore)" title="Magnolia (colore)">Magnolia</a>
</th>
<td style="background-color:#F8F4FF;">
</td>
<td style="font-family:monospace;">#F8F4FF
</td>
<td style="border-left-width:thin;">248</td>
<td>244</td>
<td>255
</td>
<td style="border-left-width:thin;">3</td>
<td>4</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">261.8</td>
<td>4.3</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Malva_(colore)" title="Malva (colore)">Malva</a>
</th>
<td style="background-color:#E0B0FF;">
</td>
<td style="font-family:monospace;">#E0B0FF
</td>
<td style="border-left-width:thin;">224</td>
<td>176</td>
<td>255
</td>
<td style="border-left-width:thin;">12</td>
<td>31</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">276</td>
<td>31</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Malva_chiaro" class="mw-redirect" title="Malva chiaro">Malva chiaro</a>
</th>
<td style="background-color:#996666;">
</td>
<td style="font-family:monospace;">#996666
</td>
<td style="border-left-width:thin;">153</td>
<td>102</td>
<td>102
</td>
<td style="border-left-width:thin;">0</td>
<td>33</td>
<td>33</td>
<td>40
</td>
<td style="border-left-width:thin;">0</td>
<td>33.3</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Mandarino_(colore)" title="Mandarino (colore)">Mandarino</a>
</th>
<td style="background-color:#FFCC00;">
</td>
<td style="font-family:monospace;">#FFCC00
</td>
<td style="border-left-width:thin;">255</td>
<td>204</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>20</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">48</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Marrone" title="Marrone">Marrone</a>
</th>
<td style="background-color:#964B00;">
</td>
<td style="font-family:monospace;">#964B00
</td>
<td style="border-left-width:thin;">150</td>
<td>75</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>50</td>
<td>100</td>
<td>41
</td>
<td style="border-left-width:thin;">30</td>
<td>100</td>
<td>59
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Marrone_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Marrone chiaro (la pagina non esiste)">Marrone chiaro</a>
</th>
<td style="background-color:#CD853F;">
</td>
<td style="font-family:monospace;">#CD853F
</td>
<td style="border-left-width:thin;">205</td>
<td>133</td>
<td>63
</td>
<td style="border-left-width:thin;">0</td>
<td>35</td>
<td>69</td>
<td>20
</td>
<td style="border-left-width:thin;">30</td>
<td>69</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Marrone_pastello" title="Marrone pastello">Marrone pastello</a>
</th>
<td style="background-color:#987654;">
</td>
<td style="font-family:monospace;">#987654
</td>
<td style="border-left-width:thin;">152</td>
<td>118</td>
<td>84
</td>
<td style="border-left-width:thin;">0</td>
<td>22</td>
<td>45</td>
<td>40
</td>
<td style="border-left-width:thin;">30</td>
<td>45</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Marrone-rosso&amp;action=edit&amp;redlink=1" class="new" title="Marrone-rosso (la pagina non esiste)">Marrone-rosso</a>
</th>
<td style="background-color:#993300;">
</td>
<td style="font-family:monospace;">#993300
</td>
<td style="border-left-width:thin;">153</td>
<td>51</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>67</td>
<td>100</td>
<td>40
</td>
<td style="border-left-width:thin;">20</td>
<td>100</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Marrone_sabbia_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Marrone sabbia chiaro (la pagina non esiste)">Marrone sabbia chiaro</a>
</th>
<td style="background-color:#DABDAB;">
</td>
<td style="font-family:monospace;">#DABDAB
</td>
<td style="border-left-width:thin;">218</td>
<td>189</td>
<td>171
</td>
<td style="border-left-width:thin;">0</td>
<td>13</td>
<td>22</td>
<td>15
</td>
<td style="border-left-width:thin;">23</td>
<td>21.6</td>
<td>85.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Marrone_scuro" class="mw-redirect" title="Marrone scuro">Marrone scuro</a>
</th>
<td style="background-color:#654321;">
</td>
<td style="font-family:monospace;">#654321
</td>
<td style="border-left-width:thin;">101</td>
<td>67</td>
<td>33
</td>
<td style="border-left-width:thin;">0</td>
<td>34</td>
<td>67</td>
<td>60
</td>
<td style="border-left-width:thin;">30</td>
<td>67.3</td>
<td>39.6
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Melanzana_(colore)" title="Melanzana (colore)">Melanzana</a>
</th>
<td style="background-color:#990066;">
</td>
<td style="font-family:monospace;">#990066
</td>
<td style="border-left-width:thin;">153</td>
<td>0</td>
<td>102
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>33</td>
<td>40
</td>
<td style="border-left-width:thin;">320</td>
<td>100</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Mogano_(colore)" title="Mogano (colore)">Mogano</a>
</th>
<td style="background-color:#C04000;">
</td>
<td style="font-family:monospace;">#C04000
</td>
<td style="border-left-width:thin;">192</td>
<td>64</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>67</td>
<td>100</td>
<td>25
</td>
<td style="border-left-width:thin;">20</td>
<td>100</td>
<td>75,3
</td></tr>
<tr>
<th style="text-align:left;"><span id="N"></span> <a href="/wiki/Nero" title="Nero">Nero</a>
</th>
<td style="background-color:#000000;">
</td>
<td style="font-family:monospace;">#000000
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0</td>
<td>100
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>0
</td></tr>
<tr>
<th style="text-align:left;"><span id="O"></span> <a href="/wiki/Ocra" title="Ocra">Ocra</a>
</th>
<td style="background-color:#CC7722;">
</td>
<td style="font-family:monospace;">#CC7722
</td>
<td style="border-left-width:thin;">204</td>
<td>119</td>
<td>34
</td>
<td style="border-left-width:thin;">0</td>
<td>42</td>
<td>83</td>
<td>20
</td>
<td style="border-left-width:thin;">30</td>
<td>83</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_oliva" title="Verde oliva">Olivina</a>
</th>
<td style="background-color:#9AB973;">
</td>
<td style="font-family:monospace;">#9AB973
</td>
<td style="border-left-width:thin;">154</td>
<td>185</td>
<td>115
</td>
<td style="border-left-width:thin;">17</td>
<td>0</td>
<td>38</td>
<td>27
</td>
<td style="border-left-width:thin;">86.6</td>
<td>37.8</td>
<td>72.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Orchidea_(colore)" title="Orchidea (colore)">Orchidea</a>
</th>
<td style="background-color:#DA70D6;">
</td>
<td style="font-family:monospace;">#DA70D6
</td>
<td style="border-left-width:thin;">218</td>
<td>112</td>
<td>214
</td>
<td style="border-left-width:thin;">0</td>
<td>49</td>
<td>2</td>
<td>15
</td>
<td style="border-left-width:thin;">302.3</td>
<td>48.6</td>
<td>85.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Oro_(colore)" title="Oro (colore)">Oro</a>
</th>
<td style="background-color:#ffd700;">
</td>
<td style="font-family:monospace;">#FFD700
</td>
<td style="border-left-width:thin;">255</td>
<td>215</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>16</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">51</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Oro_vecchio" title="Oro vecchio">Oro vecchio</a>
</th>
<td style="background-color:#CFB53B;">
</td>
<td style="font-family:monospace;">#CFB53B
</td>
<td style="border-left-width:thin;">207</td>
<td>181</td>
<td>59
</td>
<td style="border-left-width:thin;">0</td>
<td>11</td>
<td>72</td>
<td>19
</td>
<td style="border-left-width:thin;">49</td>
<td>71</td>
<td>81
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Ottone_antico_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Ottone antico (colore) (la pagina non esiste)">Ottone antico</a>
</th>
<td style="background-color:#CC9966;">
</td>
<td style="font-family:monospace;">#CC9966
</td>
<td style="border-left-width:thin;">204</td>
<td>153</td>
<td>102
</td>
<td style="border-left-width:thin;">0</td>
<td>25</td>
<td>50</td>
<td>20
</td>
<td style="border-left-width:thin;">30</td>
<td>50</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Ottanio_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Ottanio (colore) (la pagina non esiste)">Ottanio</a>
</th>
<td style="background-color:#00665C;">
</td>
<td style="font-family:monospace;">#00665C
</td>
<td style="border-left-width:thin;">0</td>
<td>40</td>
<td>36
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>10</td>
<td>60
</td>
<td style="border-left-width:thin;">174.1</td>
<td>100</td>
<td>40
</td></tr>
<tr>
<th style="text-align:left;"><span id="P"></span> <a href="/wiki/Papaya_(colore)" title="Papaya (colore)">Papaia</a>
</th>
<td style="background-color:#FFEFD5;">
</td>
<td style="font-family:monospace;">#FFEFD5
</td>
<td style="border-left-width:thin;">255</td>
<td>239</td>
<td>213
</td>
<td style="border-left-width:thin;">0</td>
<td>6</td>
<td>16</td>
<td>0
</td>
<td style="border-left-width:thin;">37.1</td>
<td>16.5</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Pera_(colore)" title="Pera (colore)">Pera</a>
</th>
<td style="background-color:#D1E231;">
</td>
<td style="font-family:monospace;">#D1E231
</td>
<td style="border-left-width:thin;">209</td>
<td>226</td>
<td>49
</td>
<td style="border-left-width:thin;">8</td>
<td>0</td>
<td>78</td>
<td>11
</td>
<td style="border-left-width:thin;">65.8</td>
<td>78.3</td>
<td>88.6
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Pervinca_(colore)" title="Pervinca (colore)">Pervinca</a>
</th>
<td style="background-color:#CCCCFF;">
</td>
<td style="font-family:monospace;">#CCCCFF
</td>
<td style="border-left-width:thin;">204</td>
<td>204</td>
<td>255
</td>
<td style="border-left-width:thin;">20</td>
<td>20</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">240</td>
<td>20</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Pesca_(colore)" class="mw-redirect" title="Pesca (colore)">Pesca</a>
</th>
<td style="background-color:#FFE5B4;">
</td>
<td style="font-family:monospace;">#FFE5B4
</td>
<td style="border-left-width:thin;">255</td>
<td>229</td>
<td>180
</td>
<td style="border-left-width:thin;">0</td>
<td>10</td>
<td>29</td>
<td>0
</td>
<td style="border-left-width:thin;">39.2</td>
<td>29.4</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Pesca_scuro_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Pesca scuro (colore) (la pagina non esiste)">Pesca scuro</a>
</th>
<td style="background-color:#FFDAB9;">
</td>
<td style="font-family:monospace;">#FFDAB9
</td>
<td style="border-left-width:thin;">255</td>
<td>218</td>
<td>185
</td>
<td style="border-left-width:thin;">0</td>
<td>15</td>
<td>27</td>
<td>0
</td>
<td style="border-left-width:thin;">28.3</td>
<td>27.5</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Pesca-arancio" class="mw-redirect" title="Pesca-arancio">Pesca-arancio</a>
</th>
<td style="background-color:#FFCC99;">
</td>
<td style="font-family:monospace;">#FFCC99
</td>
<td style="border-left-width:thin;">255</td>
<td>204</td>
<td>153
</td>
<td style="border-left-width:thin;">0</td>
<td>20</td>
<td>40</td>
<td>0
</td>
<td style="border-left-width:thin;">30</td>
<td>40</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Pesca-giallo" title="Pesca-giallo">Pesca-giallo</a>
</th>
<td style="background-color:#FADFAD;">
</td>
<td style="font-family:monospace;">#FADFAD
</td>
<td style="border-left-width:thin;">250</td>
<td>223</td>
<td>173
</td>
<td style="border-left-width:thin;">0</td>
<td>11</td>
<td>31</td>
<td>2
</td>
<td style="border-left-width:thin;">39</td>
<td>30.8</td>
<td>98
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Pistacchio_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Pistacchio (colore) (la pagina non esiste)">Pistacchio</a>
</th>
<td style="background-color:#93C572;">
</td>
<td style="font-family:monospace;">#93C572
</td>
<td style="border-left-width:thin;">147</td>
<td>197</td>
<td>114
</td>
<td style="border-left-width:thin;">25</td>
<td>0</td>
<td>42</td>
<td>23
</td>
<td style="border-left-width:thin;">96.1</td>
<td>42.1</td>
<td>77.3
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Platino_(colore)" title="Platino (colore)">Platino</a>
</th>
<td style="background-color:#E5E4E2;">
</td>
<td style="font-family:monospace;">#E5E4E2
</td>
<td style="border-left-width:thin;">229</td>
<td>228</td>
<td>226
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>1</td>
<td>10
</td>
<td style="border-left-width:thin;">40</td>
<td>1.3</td>
<td>89.8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Porpora" title="Porpora">Porpora</a>
</th>
<td style="background-color:#B20000;">
</td>
<td style="font-family:monospace;">#B20000
</td>
<td style="border-left-width:thin;">178</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">30</td>
<td>100</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>70
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Prugna_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Prugna (colore) (la pagina non esiste)">Prugna</a>
</th>
<td style="background-color:#660066;">
</td>
<td style="font-family:monospace;">#660066
</td>
<td style="border-left-width:thin;">102</td>
<td>0</td>
<td>102
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>0</td>
<td>60
</td>
<td style="border-left-width:thin;">300</td>
<td>100</td>
<td>40
</td></tr>
<tr>
<th style="text-align:left;"><span id="R"></span> <a href="/wiki/Rame_(colore)" title="Rame (colore)">Rame</a>
</th>
<td style="background-color:#b87333;">
</td>
<td style="font-family:monospace;">#B87333
</td>
<td style="border-left-width:thin;">184</td>
<td>115</td>
<td>51
</td>
<td style="border-left-width:thin;">0</td>
<td>38</td>
<td>72</td>
<td>28
</td>
<td style="border-left-width:thin;">29</td>
<td>72</td>
<td>72
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosa_(colore)" title="Rosa (colore)">Rosa</a>
</th>
<td style="background-color:#FFC0CB;">
</td>
<td style="font-family:monospace;">#FFC0CB
</td>
<td style="border-left-width:thin;">255</td>
<td>192</td>
<td>203
</td>
<td style="border-left-width:thin;">0</td>
<td>25</td>
<td>20</td>
<td>0
</td>
<td style="border-left-width:thin;">350</td>
<td>25</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosa_arancio" class="mw-redirect" title="Rosa arancio">Rosa arancio</a>
</th>
<td style="background-color:#FF9966;">
</td>
<td style="font-family:monospace;">#FF9966
</td>
<td style="border-left-width:thin;">255</td>
<td>153</td>
<td>102
</td>
<td style="border-left-width:thin;">0</td>
<td>40</td>
<td>60</td>
<td>0
</td>
<td style="border-left-width:thin;">20</td>
<td>60</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosa_medio&amp;action=edit&amp;redlink=1" class="new" title="Rosa medio (la pagina non esiste)">Rosa medio</a>
</th>
<td style="background-color:#DB244F;">
</td>
<td style="font-family:monospace;">#DB244F
</td>
<td style="border-left-width:thin;">219</td>
<td>36</td>
<td>79
</td>
<td style="border-left-width:thin;">0</td>
<td>84</td>
<td>64</td>
<td>14
</td>
<td style="border-left-width:thin;">345.9</td>
<td>83.6</td>
<td>85.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosa_Mountbatten" title="Rosa Mountbatten">Rosa Mountbatten</a>
</th>
<td style="background-color:#997A8D;">
</td>
<td style="font-family:monospace;">#997A8D
</td>
<td style="border-left-width:thin;">153</td>
<td>122</td>
<td>141
</td>
<td style="border-left-width:thin;">0</td>
<td>20</td>
<td>8</td>
<td>40
</td>
<td style="border-left-width:thin;">323.2</td>
<td>20.3</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosa_pallido&amp;action=edit&amp;redlink=1" class="new" title="Rosa pallido (la pagina non esiste)">Rosa pallido</a>
</th>
<td style="background-color:#FADADD;">
</td>
<td style="font-family:monospace;">#FADADD
</td>
<td style="border-left-width:thin;">250</td>
<td>218</td>
<td>221
</td>
<td style="border-left-width:thin;">0</td>
<td>13</td>
<td>12</td>
<td>2
</td>
<td style="border-left-width:thin;">354.4</td>
<td>12.8</td>
<td>98
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosa_pastello&amp;action=edit&amp;redlink=1" class="new" title="Rosa pastello (la pagina non esiste)">Rosa pastello</a>
</th>
<td style="background-color:#FFD1DC;">
</td>
<td style="font-family:monospace;">#FFD1DC
</td>
<td style="border-left-width:thin;">255</td>
<td>209</td>
<td>220
</td>
<td style="border-left-width:thin;">0</td>
<td>18</td>
<td>14</td>
<td>0
</td>
<td style="border-left-width:thin;">345.7</td>
<td>18</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosa_scuro" class="mw-redirect" title="Rosa scuro">Rosa scuro</a>
</th>
<td style="background-color:#E75480;">
</td>
<td style="font-family:monospace;">#E75480
</td>
<td style="border-left-width:thin;">231</td>
<td>84</td>
<td>128
</td>
<td style="border-left-width:thin;">0</td>
<td>63</td>
<td>42</td>
<td>9
</td>
<td style="border-left-width:thin;">342</td>
<td>64</td>
<td>91
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosa_shocking" title="Rosa shocking">Rosa shocking</a>
</th>
<td style="background-color:#FC0FC0;">
</td>
<td style="font-family:monospace;">#FC0FC0
</td>
<td style="border-left-width:thin;">252</td>
<td>15</td>
<td>192
</td>
<td style="border-left-width:thin;">0</td>
<td>94</td>
<td>24</td>
<td>1
</td>
<td style="border-left-width:thin;">315</td>
<td>94</td>
<td>99
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosa_(colore)" title="Rosa (colore)">Rosa vivo</a>
</th>
<td style="background-color:#FF007F;">
</td>
<td style="font-family:monospace;">#FF007F
</td>
<td style="border-left-width:thin;">255</td>
<td>0</td>
<td>127
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>50</td>
<td>0
</td>
<td style="border-left-width:thin;">330.1</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso" title="Rosso">Rosso</a>
</th>
<td style="background-color:#FF0000;">
</td>
<td style="font-family:monospace;">#FF0000
</td>
<td style="border-left-width:thin;">255</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_aragosta&amp;action=edit&amp;redlink=1" class="new" title="Rosso aragosta (la pagina non esiste)">Rosso aragosta</a>
</th>
<td style="background-color:#cc5500;">
</td>
<td style="font-family:monospace;">#CC5500
</td>
<td style="border-left-width:thin;">204</td>
<td>85</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>58</td>
<td>100</td>
<td>20
</td>
<td style="border-left-width:thin;">25</td>
<td>100</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_cardinale" title="Rosso cardinale">Rosso cardinale</a>
</th>
<td style="background-color:#C41E3A;">
</td>
<td style="font-family:monospace;">#C41E3A
</td>
<td style="border-left-width:thin;">196</td>
<td>30</td>
<td>58
</td>
<td style="border-left-width:thin;">0</td>
<td>85</td>
<td>70</td>
<td>23
</td>
<td style="border-left-width:thin;">350</td>
<td>85</td>
<td>77
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_corsa" title="Rosso corsa">Rosso corsa</a>
</th>
<td style="background-color:#CC0000;">
</td>
<td style="font-family:monospace;">#CC0000
</td>
<td style="border-left-width:thin;">204</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>100</td>
<td>20
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_Falun" title="Rosso Falun">Rosso Falun</a>
</th>
<td style="background-color:#801818;">
</td>
<td style="font-family:monospace;">#801818
</td>
<td style="border-left-width:thin;">128</td>
<td>24</td>
<td>24
</td>
<td style="border-left-width:thin;">0</td>
<td>81</td>
<td>81</td>
<td>50
</td>
<td style="border-left-width:thin;">0</td>
<td>81.3</td>
<td>50.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_fragola&amp;action=edit&amp;redlink=1" class="new" title="Rosso fragola (la pagina non esiste)">Rosso fragola</a>
</th>
<td style="background-color:#CE3018;">
</td>
<td style="font-family:monospace;">#CE3018
</td>
<td style="border-left-width:thin;">206</td>
<td>48</td>
<td>24
</td>
<td style="border-left-width:thin;">0</td>
<td>77</td>
<td>88</td>
<td>19
</td>
<td style="border-left-width:thin;">8</td>
<td>88</td>
<td>81
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_fuoco&amp;action=edit&amp;redlink=1" class="new" title="Rosso fuoco (la pagina non esiste)">Rosso fuoco</a>
</th>
<td style="background-color:#A61022;">
</td>
<td style="font-family:monospace;">#A61022
</td>
<td style="border-left-width:thin;">166</td>
<td>16</td>
<td>34
</td>
<td style="border-left-width:thin;">0</td>
<td>90</td>
<td>80</td>
<td>35
</td>
<td style="border-left-width:thin;">353</td>
<td>90</td>
<td>65
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_mattone" title="Rosso mattone">Rosso mattone</a>
</th>
<td style="background-color:#C41E3A;">
</td>
<td style="font-family:monospace;">#B22222
</td>
<td style="border-left-width:thin;">178</td>
<td>34</td>
<td>34
</td>
<td style="border-left-width:thin;">0</td>
<td>81</td>
<td>81</td>
<td>30
</td>
<td style="border-left-width:thin;">0</td>
<td>80,9</td>
<td>69,8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_mattone_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Rosso mattone chiaro (la pagina non esiste)">Rosso mattone chiaro</a>
</th>
<td style="background-color:#BD8E80;">
</td>
<td style="font-family:monospace;">#BD8E80
</td>
<td style="border-left-width:thin;">189</td>
<td>142</td>
<td>128
</td>
<td style="border-left-width:thin;">0</td>
<td>25</td>
<td>32</td>
<td>26
</td>
<td style="border-left-width:thin;">13.8</td>
<td>32.3</td>
<td>74.1
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_pomodoro&amp;action=edit&amp;redlink=1" class="new" title="Rosso pomodoro (la pagina non esiste)">Rosso pomodoro</a>
</th>
<td style="background-color:#FF6347;">
</td>
<td style="font-family:monospace;">#FF6347
</td>
<td style="border-left-width:thin;">255</td>
<td>99</td>
<td>71
</td>
<td style="border-left-width:thin;">0</td>
<td>61</td>
<td>72</td>
<td>0
</td>
<td style="border-left-width:thin;">9.1</td>
<td>72.2</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_pompeiano" title="Rosso pompeiano">Rosso pompeiano</a>
</th>
<td style="background-color:#D21F1B;">
</td>
<td style="font-family:monospace;">#D21F1B
</td>
<td style="border-left-width:thin;">210</td>
<td>31</td>
<td>27
</td>
<td style="border-left-width:thin;">0</td>
<td>85</td>
<td>87</td>
<td>18
</td>
<td style="border-left-width:thin;">1</td>
<td>87</td>
<td>82
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_rosa&amp;action=edit&amp;redlink=1" class="new" title="Rosso rosa (la pagina non esiste)">Rosso rosa</a>
</th>
<td style="background-color:#FF6088;">
</td>
<td style="font-family:monospace;">#FF6088
</td>
<td style="border-left-width:thin;">255</td>
<td>96</td>
<td>136
</td>
<td style="border-left-width:thin;">0</td>
<td>62</td>
<td>47</td>
<td>0
</td>
<td style="border-left-width:thin;">344.9</td>
<td>62.4</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_sangue_(colore)&amp;action=edit&amp;redlink=1" class="new" title="Rosso sangue (colore) (la pagina non esiste)">Rosso sangue</a>
</th>
<td style="background-color:#500000;">
</td>
<td style="font-family:monospace;">#500000
</td>
<td style="border-left-width:thin;">80</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>100</td>
<td>69
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>31.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_segnale&amp;action=edit&amp;redlink=1" class="new" title="Rosso segnale (la pagina non esiste)">Rosso segnale</a>
</th>
<td style="background-color:#A52019;">
</td>
<td style="font-family:monospace;">#A52019
</td>
<td style="border-left-width:thin;">165</td>
<td>32</td>
<td>25
</td>
<td style="border-left-width:thin;">23</td>
<td>96</td>
<td>100</td>
<td>19
</td>
<td style="border-left-width:thin;">3</td>
<td>84.8</td>
<td>64.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_Tiziano" title="Rosso Tiziano">Rosso Tiziano</a>
</th>
<td style="background-color:#BA6262;">
</td>
<td style="font-family:monospace;">#BA6262
</td>
<td style="border-left-width:thin;">186</td>
<td>98</td>
<td>98
</td>
<td style="border-left-width:thin;">0</td>
<td>47</td>
<td>47</td>
<td>27
</td>
<td style="border-left-width:thin;">0</td>
<td>47</td>
<td>73
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rosso_veneziano" title="Rosso veneziano">Rosso veneziano</a>
</th>
<td style="background-color:#C80815;">
</td>
<td style="font-family:monospace;">#C80815
</td>
<td style="border-left-width:thin;">200</td>
<td>8</td>
<td>21
</td>
<td style="border-left-width:thin;">0</td>
<td>96</td>
<td>90</td>
<td>22
</td>
<td style="border-left-width:thin;">355.9</td>
<td>96</td>
<td>78.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Rosso_violetto_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Rosso violetto chiaro (la pagina non esiste)">Rosso violetto chiaro</a>
</th>
<td style="background-color:#DB7093;">
</td>
<td style="font-family:monospace;">#DB7093
</td>
<td style="border-left-width:thin;">219</td>
<td>112</td>
<td>147
</td>
<td style="border-left-width:thin;">0</td>
<td>49</td>
<td>33</td>
<td>14
</td>
<td style="border-left-width:thin;">340.4</td>
<td>48.9</td>
<td>85.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Rubino_(colore)" title="Rubino (colore)">Rubino</a>
</th>
<td style="background-color:#B72755;">
</td>
<td style="font-family:monospace;">#B72755
</td>
<td style="border-left-width:thin;">183</td>
<td>39</td>
<td>85
</td>
<td style="border-left-width:thin;">30</td>
<td>100</td>
<td>60</td>
<td>0
</td>
<td style="border-left-width:thin;">341</td>
<td>79</td>
<td>72
</td></tr>
<tr>
<th style="text-align:left;"><span id="S"></span> <a href="/wiki/Sabbia_(colore)" class="mw-redirect" title="Sabbia (colore)">Sabbia</a>
</th>
<td style="background-color:#F4A460;">
</td>
<td style="font-family:monospace;">#F4A460
</td>
<td style="border-left-width:thin;">244</td>
<td>164</td>
<td>96
</td>
<td style="border-left-width:thin;">0</td>
<td>32</td>
<td>59</td>
<td>3
</td>
<td style="border-left-width:thin;">28</td>
<td>61</td>
<td>96
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Salmone_(colore)" class="mw-redirect" title="Salmone (colore)">Salmone</a>
</th>
<td style="background-color:#FF8C69;">
</td>
<td style="font-family:monospace;">#FF8C69
</td>
<td style="border-left-width:thin;">255</td>
<td>140</td>
<td>105
</td>
<td style="border-left-width:thin;">0</td>
<td>45</td>
<td>59</td>
<td>0
</td>
<td style="border-left-width:thin;">14</td>
<td>59</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Salmone_scuro" class="mw-redirect" title="Salmone scuro">Salmone scuro</a>
</th>
<td style="background-color:#E9967A;">
</td>
<td style="font-family:monospace;">#E9967A
</td>
<td style="border-left-width:thin;">233</td>
<td>150</td>
<td>122
</td>
<td style="border-left-width:thin;">0</td>
<td>36</td>
<td>48</td>
<td>9
</td>
<td style="border-left-width:thin;">15</td>
<td>48</td>
<td>91
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Sangria_(colore)" title="Sangria (colore)">Sangria</a>
</th>
<td style="background-color:#92000A;">
</td>
<td style="font-family:monospace;">#92000A
</td>
<td style="border-left-width:thin;">146</td>
<td>0</td>
<td>10
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>93</td>
<td>43
</td>
<td style="border-left-width:thin;">355.9</td>
<td>100</td>
<td>57.3
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Scarlatto" title="Scarlatto">Scarlatto</a>
</th>
<td style="background-color:#FF2400;">
</td>
<td style="font-family:monospace;">#FF2400
</td>
<td style="border-left-width:thin;">255</td>
<td>36</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>86</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">8</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Scarlatto_scuro&amp;action=edit&amp;redlink=1" class="new" title="Scarlatto scuro (la pagina non esiste)">Scarlatto scuro</a>
</th>
<td style="background-color:#560319;">
</td>
<td style="font-family:monospace;">#560319
</td>
<td style="border-left-width:thin;">86</td>
<td>3</td>
<td>25
</td>
<td style="border-left-width:thin;">0</td>
<td>97</td>
<td>71</td>
<td>66
</td>
<td style="border-left-width:thin;">344.1</td>
<td>96.5</td>
<td>33.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Senape_(colore)" title="Senape (colore)">Senape</a>
</th>
<td style="background-color:#FFDB58;">
</td>
<td style="font-family:monospace;">#FFDB58
</td>
<td style="border-left-width:thin;">255</td>
<td>219</td>
<td>88
</td>
<td style="border-left-width:thin;">1</td>
<td>12</td>
<td>77</td>
<td>0
</td>
<td style="border-left-width:thin;">33</td>
<td>255</td>
<td>172
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Seppia_(colore)" title="Seppia (colore)">Seppia</a>
</th>
<td style="background-color:#704214;">
</td>
<td style="font-family:monospace;">#704214
</td>
<td style="border-left-width:thin;">112</td>
<td>66</td>
<td>20
</td>
<td style="border-left-width:thin;">0</td>
<td>41</td>
<td>82</td>
<td>56
</td>
<td style="border-left-width:thin;">30</td>
<td>82</td>
<td>44
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Solidago_(colore)" title="Solidago (colore)">Solidago</a>
</th>
<td style="background-color:#DAA520;">
</td>
<td style="font-family:monospace;">#DAA520
</td>
<td style="border-left-width:thin;">218</td>
<td>165</td>
<td>32
</td>
<td style="border-left-width:thin;">0</td>
<td>24</td>
<td>85</td>
<td>15
</td>
<td style="border-left-width:thin;">42.9</td>
<td>85.3</td>
<td>85.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Solidago_scuro" class="mw-redirect" title="Solidago scuro">Solidago scuro</a>
</th>
<td style="background-color:#B8860B;">
</td>
<td style="font-family:monospace;">#B8860B
</td>
<td style="border-left-width:thin;">184</td>
<td>134</td>
<td>11
</td>
<td style="border-left-width:thin;">0</td>
<td>27</td>
<td>94</td>
<td>28
</td>
<td style="border-left-width:thin;">42.7</td>
<td>94</td>
<td>72.2
</td></tr>
<tr>
<th style="text-align:left;"><span id="T"></span> <a href="/wiki/Tanno_(colore)" title="Tanno (colore)">Tanno</a>
</th>
<td style="background-color:#D2B48C;">
</td>
<td style="font-family:monospace;">#D2B48C
</td>
<td style="border-left-width:thin;">210</td>
<td>180</td>
<td>140
</td>
<td style="border-left-width:thin;">0</td>
<td>14</td>
<td>33</td>
<td>18
</td>
<td style="border-left-width:thin;">34.3</td>
<td>33.3</td>
<td>82.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Tenn%C3%A9" title="Tenné">Tenné</a>
</th>
<td style="background-color:#CD5700;">
</td>
<td style="font-family:monospace;">#CD5700
</td>
<td style="border-left-width:thin;">205</td>
<td>87</td>
<td>140
</td>
<td style="border-left-width:thin;">0</td>
<td>58</td>
<td>100</td>
<td>20
</td>
<td style="border-left-width:thin;">25.5</td>
<td>100</td>
<td>80.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Terra_d%27ombra" title="Terra d'ombra">Terra d'ombra</a>
</th>
<td style="background-color:#635147;">
</td>
<td style="font-family:monospace;">#635147
</td>
<td style="border-left-width:thin;">99</td>
<td>81</td>
<td>71
</td>
<td style="border-left-width:thin;">0</td>
<td>18</td>
<td>28</td>
<td>61
</td>
<td style="border-left-width:thin;">21.4</td>
<td>28.3</td>
<td>38.8
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Terra_d%27ombra_bruciata" class="mw-redirect" title="Terra d'ombra bruciata">Terra d'ombra bruciata</a>
</th>
<td style="background-color:#8A3324;">
</td>
<td style="font-family:monospace;">#8A3324
</td>
<td style="border-left-width:thin;">138</td>
<td>51</td>
<td>36
</td>
<td style="border-left-width:thin;">0</td>
<td>63</td>
<td>74</td>
<td>46
</td>
<td style="border-left-width:thin;">8.8</td>
<td>73.9</td>
<td>54.1
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Terra_di_Siena" title="Terra di Siena">Terra di Siena</a>
</th>
<td style="background-color:#E97451;">
</td>
<td style="font-family:monospace;">#E97451
</td>
<td style="border-left-width:thin;">233</td>
<td>116</td>
<td>81
</td>
<td style="border-left-width:thin;">0</td>
<td>50</td>
<td>65</td>
<td>9
</td>
<td style="border-left-width:thin;">14</td>
<td>65</td>
<td>91
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Terra_di_Siena_bruciata" class="mw-redirect" title="Terra di Siena bruciata">Terra di Siena bruciata</a>
</th>
<td style="background-color:#531B00;">
</td>
<td style="font-family:monospace;">#531B00
</td>
<td style="border-left-width:thin;">83</td>
<td>27</td>
<td>0
</td>
<td style="border-left-width:thin;">39</td>
<td>84</td>
<td>93</td>
<td>62
</td>
<td style="border-left-width:thin;">20</td>
<td>100</td>
<td>33
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Testa_di_moro_(colore)" title="Testa di moro (colore)">Testa di moro</a>
</th>
<td style="background-color:#754909;">
</td>
<td style="font-family:monospace;">#754909
</td>
<td style="border-left-width:thin;">117</td>
<td>73</td>
<td>9
</td>
<td style="border-left-width:thin;">0</td>
<td>38</td>
<td>92</td>
<td>54
</td>
<td style="border-left-width:thin;">35.6</td>
<td>92.3</td>
<td>45.9
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/T%C3%A8_verde_(colore)" title="Tè verde (colore)">Tè verde</a>
</th>
<td style="background-color:#D0F0C0;">
</td>
<td style="font-family:monospace;">#D0F0C0
</td>
<td style="border-left-width:thin;">208</td>
<td>240</td>
<td>192
</td>
<td style="border-left-width:thin;">11</td>
<td>0</td>
<td>18</td>
<td>4
</td>
<td style="border-left-width:thin;">100</td>
<td>20</td>
<td>94
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Tronco_(colore)" title="Tronco (colore)">Tronco</a>
</th>
<td style="background-color:#79443B;">
</td>
<td style="font-family:monospace;">#79443B
</td>
<td style="border-left-width:thin;">121</td>
<td>68</td>
<td>59
</td>
<td style="border-left-width:thin;">0</td>
<td>44</td>
<td>51</td>
<td>53
</td>
<td style="border-left-width:thin;">8.7</td>
<td>51.2</td>
<td>47.5
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Turchese_(colore)" title="Turchese (colore)">Turchese</a>
</th>
<td style="background-color:#30D5C8;">
</td>
<td style="font-family:monospace;">#30D5C8
</td>
<td style="border-left-width:thin;">48</td>
<td>213</td>
<td>200
</td>
<td style="border-left-width:thin;">77</td>
<td>0</td>
<td>6</td>
<td>16
</td>
<td style="border-left-width:thin;">175</td>
<td>77</td>
<td>84
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Turchese_chiaro" class="mw-redirect" title="Turchese chiaro">Turchese chiaro</a>
</th>
<td style="background-color:#08E8DE;">
</td>
<td style="font-family:monospace;">#08E8DE
</td>
<td style="border-left-width:thin;">8</td>
<td>232</td>
<td>222
</td>
<td style="border-left-width:thin;">97</td>
<td>0</td>
<td>4</td>
<td>9
</td>
<td style="border-left-width:thin;">177</td>
<td>97</td>
<td>91
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Turchese_pallido" class="mw-redirect" title="Turchese pallido">Turchese pallido</a>
</th>
<td style="background-color:#99FFCC;">
</td>
<td style="font-family:monospace;">#99FFCC
</td>
<td style="border-left-width:thin;">153</td>
<td>255</td>
<td>204
</td>
<td style="border-left-width:thin;">40</td>
<td>0</td>
<td>20</td>
<td>0
</td>
<td style="border-left-width:thin;">150</td>
<td>40</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Turchese_scuro" class="mw-redirect" title="Turchese scuro">Turchese scuro</a>
</th>
<td style="background-color:#116062;">
</td>
<td style="font-family:monospace;">#116062
</td>
<td style="border-left-width:thin;">17</td>
<td>96</td>
<td>98
</td>
<td style="border-left-width:thin;">83</td>
<td>2</td>
<td>0</td>
<td>62
</td>
<td style="border-left-width:thin;">181.5</td>
<td>82.7</td>
<td>38.4
</td></tr>
<tr>
<th style="text-align:left;"><span id="U"></span> <a href="/wiki/Uovo_di_pettirosso" title="Uovo di pettirosso">Uovo di pettirosso</a>
</th>
<td style="background-color:#00CCCC;">
</td>
<td style="font-family:monospace;">#00CCCC
</td>
<td style="border-left-width:thin;">0</td>
<td>204</td>
<td>204
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>0</td>
<td>20
</td>
<td style="border-left-width:thin;">180</td>
<td>100</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Uovo_di_pettirosso_chiaro" class="mw-redirect" title="Uovo di pettirosso chiaro">Uovo di pettirosso chiaro</a>
</th>
<td style="background-color:#96DED1;">
</td>
<td style="font-family:monospace;">#96DED1
</td>
<td style="border-left-width:thin;">150</td>
<td>222</td>
<td>209
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>0</td>
<td>20
</td>
<td style="border-left-width:thin;">169</td>
<td>32</td>
<td>87
</td></tr>
<tr>
<th style="text-align:left;"><span id="V"></span> <a href="/wiki/Verde" title="Verde">Verde</a>
</th>
<td style="background-color:#00ff00;">
</td>
<td style="font-family:monospace;">#00FF00
</td>
<td style="border-left-width:thin;">0</td>
<td>255</td>
<td>0
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">120</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_Caraibi" class="mw-redirect" title="Verde Caraibi">Verde Caraibi</a>
</th>
<td style="background-color:#00CC99;">
</td>
<td style="font-family:monospace;">#00CC99
</td>
<td style="border-left-width:thin;">0</td>
<td>204</td>
<td>153
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>25</td>
<td>20
</td>
<td style="border-left-width:thin;">165</td>
<td>100</td>
<td>80
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_foresta" title="Verde foresta">Verde foresta</a>
</th>
<td style="background-color:#228b22;">
</td>
<td style="font-family:monospace;">#228B22
</td>
<td style="border-left-width:thin;">34</td>
<td>139</td>
<td>34
</td>
<td style="border-left-width:thin;">83</td>
<td>21</td>
<td>100</td>
<td>8
</td>
<td style="border-left-width:thin;">120</td>
<td>76</td>
<td>55
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_chiaro" title="Verde chiaro">Verde chiaro</a>
</th>
<td style="background-color:#66FF00;">
</td>
<td style="font-family:monospace;">#66FF00
</td>
<td style="border-left-width:thin;">102</td>
<td>255</td>
<td>0
</td>
<td style="border-left-width:thin;">60</td>
<td>0</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">96</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde-giallo" title="Verde-giallo">Verde-giallo</a>
</th>
<td style="background-color:#ADFF2F;">
</td>
<td style="font-family:monospace;">#ADFF2F
</td>
<td style="border-left-width:thin;">173</td>
<td>255</td>
<td>47
</td>
<td style="border-left-width:thin;">32</td>
<td>0</td>
<td>82</td>
<td>0
</td>
<td style="border-left-width:thin;">83.7</td>
<td>81.6</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_marino" title="Verde marino">Verde marino</a>
</th>
<td style="background-color:#2E8B57;">
</td>
<td style="font-family:monospace;">#2E8B57
</td>
<td style="border-left-width:thin;">46</td>
<td>139</td>
<td>87
</td>
<td style="border-left-width:thin;">70</td>
<td>0</td>
<td>40</td>
<td>45
</td>
<td style="border-left-width:thin;">103</td>
<td>50</td>
<td>55
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_marino" title="Verde marino">Verde marino medio</a>
</th>
<td style="background-color:#3CB371;">
</td>
<td style="font-family:monospace;">#3CB371
</td>
<td style="border-left-width:thin;">60</td>
<td>179</td>
<td>113
</td>
<td style="border-left-width:thin;">66</td>
<td>0</td>
<td>37</td>
<td>30
</td>
<td style="border-left-width:thin;">146.7</td>
<td>66.5</td>
<td>70.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_marino" title="Verde marino">Verde marino scuro</a>
</th>
<td style="background-color:#8FBC8F;">
</td>
<td style="font-family:monospace;">#8FBC8F
</td>
<td style="border-left-width:thin;">143</td>
<td>188</td>
<td>143
</td>
<td style="border-left-width:thin;">24</td>
<td>0</td>
<td>24</td>
<td>26
</td>
<td style="border-left-width:thin;">120</td>
<td>23.9</td>
<td>73.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_menta" title="Verde menta">Verde menta</a>
</th>
<td style="background-color:#98FF98;">
</td>
<td style="font-family:monospace;">#98FF98
</td>
<td style="border-left-width:thin;">152</td>
<td>255</td>
<td>152
</td>
<td style="border-left-width:thin;">40</td>
<td>0</td>
<td>40</td>
<td>0
</td>
<td style="border-left-width:thin;">120</td>
<td>40.4</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_menta" title="Verde menta">Verde menta chiaro</a>
</th>
<td style="background-color:#A6FBB2;">
</td>
<td style="font-family:monospace;">#A6FBB2
</td>
<td style="border-left-width:thin;">166</td>
<td>251</td>
<td>178
</td>
<td style="border-left-width:thin;">34</td>
<td>0</td>
<td>29</td>
<td>2
</td>
<td style="border-left-width:thin;">128.5</td>
<td>33.9</td>
<td>98.4
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_muschio" title="Verde muschio">Verde muschio</a>
</th>
<td style="background-color:#ADDFAD;">
</td>
<td style="font-family:monospace;">#ADDFAD
</td>
<td style="border-left-width:thin;">173</td>
<td>223</td>
<td>173
</td>
<td style="border-left-width:thin;">20</td>
<td>0</td>
<td>22</td>
<td>13
</td>
<td style="border-left-width:thin;">120</td>
<td>22</td>
<td>87
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_oliva" title="Verde oliva">Verde oliva</a>
</th>
<td style="background-color:#808000;">
</td>
<td style="font-family:monospace;">#808000
</td>
<td style="border-left-width:thin;">128</td>
<td>128</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>0</td>
<td>100</td>
<td>50
</td>
<td style="border-left-width:thin;">60</td>
<td>100</td>
<td>50
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_oliva" title="Verde oliva">Verde olivastro</a>
</th>
<td style="background-color:#6B8E23;">
</td>
<td style="font-family:monospace;">#6B8E23
</td>
<td style="border-left-width:thin;">107</td>
<td>142</td>
<td>35
</td>
<td style="border-left-width:thin;">25</td>
<td>0</td>
<td>75</td>
<td>44
</td>
<td style="border-left-width:thin;">79.6</td>
<td>75.4</td>
<td>55.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_oliva" title="Verde oliva">Verde oliva scuro</a>
</th>
<td style="background-color:#556B2F;">
</td>
<td style="font-family:monospace;">#556B2F
</td>
<td style="border-left-width:thin;">85</td>
<td>107</td>
<td>47
</td>
<td style="border-left-width:thin;">21</td>
<td>0</td>
<td>56</td>
<td>58
</td>
<td style="border-left-width:thin;">82</td>
<td>56.1</td>
<td>42
</td></tr>
<tr>
<th style="text-align:left;">Verde pastello
</th>
<td style="background-color:#77DD77;">
</td>
<td style="font-family:monospace;">#77DD77
</td>
<td style="border-left-width:thin;">119</td>
<td>221</td>
<td>119
</td>
<td style="border-left-width:thin;">46</td>
<td>0</td>
<td>46</td>
<td>13
</td>
<td style="border-left-width:thin;">120</td>
<td>46.2</td>
<td>86.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_pino" title="Verde pino">Verde pino</a>
</th>
<td style="background-color:#01796F;">
</td>
<td style="font-family:monospace;">#01796F
</td>
<td style="border-left-width:thin;">1</td>
<td>121</td>
<td>111
</td>
<td style="border-left-width:thin;">99</td>
<td>0</td>
<td>8</td>
<td>53
</td>
<td style="border-left-width:thin;">175</td>
<td>99</td>
<td>47
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_primavera" title="Verde primavera">Verde primavera</a>
</th>
<td style="background-color:#00FF7F;">
</td>
<td style="font-family:monospace;">#00FF7F
</td>
<td style="border-left-width:thin;">0</td>
<td>255</td>
<td>127
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>50</td>
<td>0
</td>
<td style="border-left-width:thin;">149.9</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_primavera_scuro" class="mw-redirect" title="Verde primavera scuro">Verde primavera scuro</a>
</th>
<td style="background-color:#177245;">
</td>
<td style="font-family:monospace;">#177245
</td>
<td style="border-left-width:thin;">23</td>
<td>114</td>
<td>69
</td>
<td style="border-left-width:thin;">80</td>
<td>0</td>
<td>39</td>
<td>55
</td>
<td style="border-left-width:thin;">150.3</td>
<td>79.8</td>
<td>44.7
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_ufficio" title="Verde ufficio">Verde ufficio</a>
</th>
<td style="background-color:#008000;">
</td>
<td style="font-family:monospace;">#008000
</td>
<td style="border-left-width:thin;">0</td>
<td>128</td>
<td>0
</td>
<td style="border-left-width:thin;">100</td>
<td>0</td>
<td>100</td>
<td>50
</td>
<td style="border-left-width:thin;">120</td>
<td>100</td>
<td>50.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_smeraldo" title="Verde smeraldo">Verde smeraldo</a>
</th>
<td style="background-color:#50c878;">
</td>
<td style="font-family:monospace;">#50C878
</td>
<td style="border-left-width:thin;">80</td>
<td>200</td>
<td>120
</td>
<td style="border-left-width:thin;">60</td>
<td>0</td>
<td>40</td>
<td>22
</td>
<td style="border-left-width:thin;">140</td>
<td>60</td>
<td>78
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Verde_Veronese" title="Verde Veronese">Verde Veronese</a>
</th>
<td style="background-color:#40826D;">
</td>
<td style="font-family:monospace;">#40826D
</td>
<td style="border-left-width:thin;">64</td>
<td>130</td>
<td>109
</td>
<td style="border-left-width:thin;">51</td>
<td>0</td>
<td>16</td>
<td>49
</td>
<td style="border-left-width:thin;">161</td>
<td>51</td>
<td>51
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Vermiglio_(colore)" class="mw-redirect" title="Vermiglio (colore)">Vermiglio</a>
</th>
<td style="background-color:#FF4D00;">
</td>
<td style="font-family:monospace;">#FF4D00
</td>
<td style="border-left-width:thin;">255</td>
<td>77</td>
<td>0
</td>
<td style="border-left-width:thin;">0</td>
<td>70</td>
<td>100</td>
<td>0
</td>
<td style="border-left-width:thin;">18</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Viola_(colore)" title="Viola (colore)">Viola</a>
</th>
<td style="background-color:#800080;">
</td>
<td style="font-family:monospace;">#800080
</td>
<td style="border-left-width:thin;">128</td>
<td>0</td>
<td>128
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>0</td>
<td>50
</td>
<td style="border-left-width:thin;">300</td>
<td>100</td>
<td>50.2
</td></tr>
<tr>
<th style="text-align:left;"><a href="/w/index.php?title=Viola_chiaro&amp;action=edit&amp;redlink=1" class="new" title="Viola chiaro (la pagina non esiste)">Viola chiaro</a>
</th>
<td style="background-color:#9F00FF;">
</td>
<td style="font-family:monospace;">#9F00FF
</td>
<td style="border-left-width:thin;">159</td>
<td>0</td>
<td>255
</td>
<td style="border-left-width:thin;">38</td>
<td>100</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">277.4</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Viola_melanzana" title="Viola melanzana">Viola melanzana</a>
</th>
<td style="background-color:#991199;">
</td>
<td style="font-family:monospace;">#991199
</td>
<td style="border-left-width:thin;">153</td>
<td>17</td>
<td>153
</td>
<td style="border-left-width:thin;">0</td>
<td>89</td>
<td>0</td>
<td>40
</td>
<td style="border-left-width:thin;">300</td>
<td>88.9</td>
<td>60
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Violetto" title="Violetto">Violetto</a>
</th>
<td style="background-color:#8000FF;">
</td>
<td style="font-family:monospace;">#8000FF
</td>
<td style="border-left-width:thin;">128</td>
<td>0</td>
<td>255
</td>
<td style="border-left-width:thin;">49</td>
<td>100</td>
<td>0</td>
<td>0
</td>
<td style="border-left-width:thin;">270</td>
<td>100</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Vinaccia_(colore)" title="Vinaccia (colore)">Vinaccia</a>
</th>
<td style="background-color:#C0007F;">
</td>
<td style="font-family:monospace;">#C0007F
</td>
<td style="border-left-width:thin;">192</td>
<td>0</td>
<td>127
</td>
<td style="border-left-width:thin;">0</td>
<td>100</td>
<td>34</td>
<td>25
</td>
<td style="border-left-width:thin;">320.3</td>
<td>100</td>
<td>75.3
</td></tr>
<tr>
<th style="text-align:left;"><span id="Z"></span> <a href="/wiki/Zafferano_(colore)" title="Zafferano (colore)">Zafferano</a>
</th>
<td style="background-color:#F4C430;">
</td>
<td style="font-family:monospace;">#F4C430
</td>
<td style="border-left-width:thin;">244</td>
<td>196</td>
<td>48
</td>
<td style="border-left-width:thin;">0</td>
<td>20</td>
<td>80</td>
<td>40
</td>
<td style="border-left-width:thin;">45</td>
<td>80</td>
<td>96
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Zafferano_profondo" class="mw-redirect" title="Zafferano profondo">Zafferano profondo</a>
</th>
<td style="background-color:#FF9933;">
</td>
<td style="font-family:monospace;">#FF9933
</td>
<td style="border-left-width:thin;">255</td>
<td>153</td>
<td>51
</td>
<td style="border-left-width:thin;">0</td>
<td>40</td>
<td>80</td>
<td>0
</td>
<td style="border-left-width:thin;">30</td>
<td>80</td>
<td>100
</td></tr>
<tr>
<th style="text-align:left;"><a href="/wiki/Zaffiro_(colore)" class="mw-redirect" title="Zaffiro (colore)">Zaffiro</a>
</th>
<td style="background-color:#0F52BA;">
</td>
<td style="font-family:monospace;">#0F52BA
</td>
<td style="border-left-width:thin;">15</td>
<td>82</td>
<td>186
</td>
<td style="border-left-width:thin;">92</td>
<td>56</td>
<td>0</td>
<td>27
</td>
<td style="border-left-width:thin;">216.5</td>
<td>91.9</td>
<td>72.9
</td></tr></tbody><tfoot></tfoot></table>'''

soup = BeautifulSoup(html_content, 'html.parser')

# Initialize an empty dictionary to store colors and their hex values
colors_dict = {}

# Function to check if a character is a vowel
def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char.lower() in vowels

# Iterate through each row in the table
for row in soup.find_all('tr'):
    color_name_tag = row.th
    if color_name_tag and color_name_tag.a:
        color_name = color_name_tag.a.text.strip()
        hex_value_tag = row.find('td', style="font-family:monospace;")
        if hex_value_tag:
            hex_value = hex_value_tag.text.strip()
            colors_dict[color_name] = hex_value

            # Check if the color name ends with a vowel
            if is_vowel(color_name[-1]):
                astro = color_name[:-1] + "astro"
                colors_dict[astro] = hex_value

                accio = color_name[:-1] + "accio"
                colors_dict[accio] = hex_value

                ino = color_name[:-1] + "ino"
                colors_dict[ino] = hex_value

                if color_name[-1] == "o":
                    femminile = color_name[:-1] + "a"
                    colors_dict[femminile] = hex_value

                    astra = color_name[:-1] + "astra"
                    colors_dict[astra] = hex_value

                    accia = color_name[:-1] + "accia"
                    colors_dict[accia] = hex_value

                    ina = color_name[:-1] + "ina"
                    colors_dict[ina] = hex_value

# Convert the dictionary to JSON format
colors_json = json.dumps(colors_dict, indent=4)

# Export the dictionary to a JSON file
with open('colors.json', 'w') as json_file:
    json.dump(colors_dict, json_file, indent=4)

print("JSON exported to 'colors.json'")

print(colors_json)