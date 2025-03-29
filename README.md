# **my endless-sky-plugins**
I aim at developing small, modular and maximal compatible plugins that don't break vanilla lore too much. <br>
Please excuse bad English, spelling, grammar, etc... English isn't my mother tongue. Feel free to correct me.<br>
<a href="https://github.com/zuckung/endless-sky-plugins/pulls">Pull requests</a>, <a href="https://github.com/zuckung/endless-sky-plugins/discussions">discussions</a> and <a href="https://github.com/zuckung/endless-sky-plugins/issues">Issue reports</a> are welcome! <br>
<br>
Furthermore, I'd like to present <a href="https://zuckung.github.io/ES-DataParser/">https://zuckung.github.io/ES-DataParser/</a> to other plugin creators or people who seek information inside the data folder. Basically it is a very fast website to view every object of the data folder, especially when you don't know where to find something. For an easier browsing and comparing of game objects, like missions, ships, systems, and others.<br>
<a href="https://raw.githubusercontent.com/zuckung/ES-DataParser/master/res/parser1.jpg"><img src='https://raw.githubusercontent.com/zuckung/ES-DataParser/master/res/parser1.jpg' width='300'></a>    <a href="https://raw.githubusercontent.com/zuckung/ES-DataParser/master/res/parser2.jpg"><img src='https://raw.githubusercontent.com/zuckung/ES-DataParser/master/res/parser2.jpg' width='300'></a><br>
<br>
<br>
If you are familiar with Python, the scripts in the <a href="tools/README.md">tools-folder</a> might be interesting. There are a few to generate some of my plugins (to keep them up-to-date). And others like an ES jpg map creator or a PR files downloader.<br>
<br>
I've got another new project, a github repository that lets you online generate a galaxy with up to 500 star systems and some more options to configurate that galaxy. When done, you can download it as a plugin. Here is the link. <a href="https://github.com/zuckung/ES-GalaxyGenerator">https://github.com/zuckung/ES-GalaxyGenerator</a><br>
<br>
<a href="https://img.shields.io/"><img src="https://img.shields.io/github/downloads/zuckung/endless-sky-plugins/total"></a>
<a href="https://img.shields.io/"><img src="https://img.shields.io/github/directory-file-count/zuckung/endless-sky-plugins/myplugins?label=plugins"></a>

<a href="https://github.com/zuckung/endless-sky-plugins/blob/main/license"><img src="https://img.shields.io/github/license/zuckung/endless-sky-plugins"></a>
<a href="https://github.com/zuckung/endless-sky-plugins/commits/main"><img src="https://img.shields.io/github/last-commit/zuckung/endless-sky-plugins/main"></a>
<a href="https://github.com/zuckung/endless-sky-plugins/commits/main"><img src="https://img.shields.io/github/commit-activity/t/zuckung/endless-sky-plugins"></a>
<a href="https://github.com/zuckung/endless-sky-plugins/archive/refs/heads/main.zip"><img src="https://img.shields.io/github/repo-size/zuckung/endless-sky-plugins"></a>
<a href="https://img.shields.io/"><img src="https://img.shields.io/github/languages/code-size/zuckung/endless-sky-plugins"></a>
<a href="https://img.shields.io/"><img src="https://img.shields.io/github/languages/top/zuckung/endless-sky-plugins"></a>
<br>

## Latest News:
<table><tr><td><img width="882" height="1"><br>2025-03-29 | update: additional.command.buttons.radial<br>
2025-03-14 | update: additional.command.buttons.radial<br>
2025-03-14 | update: highrollers.ltd<br>
2025-03-11 | update: highrollers.ltd<br>
2025-03-11 | update: gegno.pirates<br>
2025-02-28 | update: additional.command.buttons.radial<br>
2025-02-26 | update: mission.helper<br>
2025-02-23 | update: additional.command.buttons.radial<br>
2025-02-20 | update: mission.helper<br>
2025-02-17 | update: mission.helper<br>
<img width="882" height="1"><br></td></tr></table>

## Plugin List:<br>
<table><tr valign="top"><td><img width="294" height="1"><br>
<a href="README.md#additionalcommandbuttonsradial">additional.command.buttons.radial</a><br>
<a href="README.md#automatadestruction0percent">automata.destruction.0percent</a><br>
<img width="294" height="1"><br></td><td><img width="294" height="1"><br>
<a href="README.md#automatainhumanspace">automata.in.human.space</a><br>
<img width="294" height="1"><br></td><td><img width="294" height="1"><br>
<a href="README.md#betterstarts">better.starts</a><br>
<img width="294" height="1"><br></td></tr></table>





---

### additional.command.buttons.radial

<img src="myplugins/additional.command.buttons.radial/icon.png" height="100">

[additional.command.buttons.radial.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0.20-additional.command.buttons.radial/additional.command.buttons.radial.zip) | N/A | N/A | [view files](https://github.com/zuckungtest/endless-sky-plugins/tree/main/myplugins/additional.command.buttons.radial/) | <a href="res/imagemd/additional.command.buttons.radial.md">view images</a> [47]<br>
%downloadcount%<br>
<br>
>Reworks the main buttons ui on the lower right side. Made for the ANDROID version of ES. See the README for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### additional.command.buttons <br>

<br>

Reworks the main buttons ui on the lower right side. Made for the ANDROID version of ES.<br> 

<br>

<br>

This plugin<br>

- rearranges and resizes some of the buttons<br>

- changes most icons (making a ring around as a standard)

- adds more permanent buttons from the radial menus to make them easy accessible<br>

- removes the radial menus<br>

- adds a new button row to the top right for the fleet commands<br>

- adds zoom buttons<br>

- adds more targeting buttons<br>

- greyes out inactive buttons<br>

- puts images behind the buttons, to grey out unavailable.<br>

- changes the ship hud<br>

<br>

<br>

<br>

Changelog:<br>

<br>

2025-03-14<br>

added reverse thrust/afterburner button to bottom left<br>

<br>

2025-02-28<br>

moved the fleet box below the text box<br>

adjusted onscreen joystick size<br>

<br>

2025-02-23<br>

added new fleet jump button<br>

moved targeting buttons to the lower right<br>

removed fleet attack from normal attack button<br>

removed targeting button from target display<br>

<br>

2025-02-06<br>

the targeting buttons blocked the new scanner attribute display, so i moved it up<br>

hollowed and colorized the targeting buttons<br>

<br>

2025-02-04<br>

increased the size of the fuel, energy and heat bar to handle fuel up to 4400<br>

resized message box to not overlap with 2 rows of escorts<br>

restored the somehow missing tactical information display<br>

added "target nearest enemy" and "target nearest asteroid" buttons<br>

removed the color folders, white is enough<br>

<br>

2024-12-28<br>

moved the ammo box to the left side if the lower buttons<br>

added ship hud (inspired by Upmost Bsc | https://github.com/tobersj/Central-HUD)<br>

<br>

2024-11-20<br>

added small main menu button to the top left corner (requested by tarminu)<br>

<br>

2024-11-02<br>

removed hold fire button, because it's unsure when/if it comes back<br>

changed fast forward button back to small again, because it messed up the mission overview<br>

added 5 colour schemes(red, green, blue, purple, orange)

<br>

2024-10-29<br>

deactivated hold fire button, because it got removed in 0.10.10<br>

<br>

2024-10-11<br>

added fleet formations button<br>

<br>

2024-10-07<br>

added fleet hold fire button<br>

<br>

2024-09-06<br>

fine tuning for the graphics<br>

<br>

2024-09-02<br>

fixed button radius typo on fleet gather<br>

moved the fleet commands to the right side, so the jump systems are better seen<br>

<br>

2024-08-31<br>

changed button background to look more natural<br>

<br>

2024-08-30<br>

fixed an error<br>

adjusted positions<br>

added zoom buttons<br>

all buttons are visible now, but greyed out if you can't use them<br>

reworked all buttons to display a ring around them<br>

resized the fast forward button in the upper left corner, and added a greyed out version<br>

<br>

2024-08-25<br>

added a new panel for the fleet commands to the top center<br>

reworked the toggle ammo button<br>

removed the expandable radial menus, because all buttons are on the screen now<br>

exchanged some of the button positions<br>

<br>

2024-05-09<br>

initial release<br>
</blockquote>
</details>
<br>
screenshots(click to enlarge):<br>
<table>
	<tr>
		<td><img src="https://raw.githubusercontent.com/zuckung/endless-sky-plugins/master/screenshots/additional.command.buttons.radial01.jpg" width="200"></td>
	</tr>
</table>
<br>

<br>


---

### automata.destruction.0percent

<img src="myplugins/automata.destruction.0percent/icon.png" height="100">

[automata.destruction.0percent.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0.1-automata.destruction.0percent/automata.destruction.0percent.zip) | 44.08 kb | 2024-06-07 | [view files](https://github.com/zuckungtest/endless-sky-plugins/tree/main/myplugins/automata.destruction.0percent/) | <a href="res/imagemd/automata.destruction.0percent.md">view images</a> [1]<br>
%downloadcount%<br>
<br>
>Modifies the self destruction chance of Sestor and Mereti ships to a value of 0.0 (0%). See the README for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### automata.destruction.0percent

<br>

<br>

Modifies the self destruction chance of Sestor and Mereti ships to a value of 0.0 (0%).<br>

<br>

Sestor 349/109/78/71/53/27/14 and Mereti 512/256/128/64/32/16/8 ships have a self destruction value of 0.0 (0%) now.<br>

You can easily change the values in automata.txt for each ship ('"self destruct" .0') to a value of your choice. I.e. 0.12 is 23%, 0.3 is 51%, 0.5 is 75%. Its calculated twice, first the chance for self destruction on boarding(i.e. 0.3) is 30%, then of the remaining 70% again 30% chance for self destruction on capturing. That makes 30% + 21% = 51% overall chance for self destruction on a capturing try.<br>

<br>

<br>

Changelog:<br>

<br>

2024-06-07<br>

text corrections (thx to TheGiraffe3)<br>

<br>

2023-10-17<br>

added plugin.txt<br>

<br>

2023-09-07<br>

changed icon<br>

changed about.txt<br>

changed readme<br>

















</blockquote>
</details>

<br>


---

### automata.in.human.space

<img src="myplugins/automata.in.human.space/icon.png" height="100">

[automata.in.human.space.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0.1-automata.in.human.space/automata.in.human.space.zip) | 35.86 kb | 2024-09-24 | [view files](https://github.com/zuckungtest/endless-sky-plugins/tree/main/myplugins/automata.in.human.space/) | <a href="res/imagemd/automata.in.human.space.md">view images</a> [1]<br>
%downloadcount%<br>
<br>
>Brings jump drive equipped automata into human space after the wanderer campaign. See the README for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### automata.in.human.space

<br>

<br>

Brings jump drive equipped automata into human space after the wanderer campaign. <br>

<br>

You can find them where Korath ships in human space are usually found(ember waste and eastern syndicate). <br>

The chance to encounter previous Korath ships or automata is like 50/50. <br>

<br>

<br>

Changelog:<br>

<br>

2024-09-24<br>

removed jumpdrive from fighters and drones and put them correctly into the carriers<br>

adjusted some fleet variants<br>

<br>

2023-10-17<br>

added plugin.txt<br>

<br>

2023-09-01<br>

added more fleet variants <br>

reworked readme <br>

changed icon.png<br>

</blockquote>
</details>

<br>


---

### better.starts

<img src="myplugins/better.starts/icon.png" height="100">

[better.starts.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0.4-better.starts/better.starts.zip) | 23.58 kb | 2024-12-19 | [view files](https://github.com/zuckungtest/endless-sky-plugins/tree/main/myplugins/better.starts/) | <a href="res/imagemd/better.starts.md">view images</a> [1]<br>
%downloadcount%<br>
<br>
>Adds several new start options with different ships, background stories, credits and debts. See the README for details.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>### better.starts <br>

<br>

Adds several new start options with different ships, background stories, credits and debts.<br>

<br>

<ul>

<li>Start: Trader | Freighter: equipped for cargo transport, in Merak system</li>

<li>Start: Trader (Hai) | Aphid: equipped for cargo transport, in Fah Soom system(Hai space)</li>

<li>Start: Passenger Transport | Scout: equipped for passenger transport, Talita system</li>

<li>Start: Miner | Sunder: equipped for mining, in Rasalhague system</li>

<li>Start: Salvager | Shuttle: equipped for boarding, in Aldhibain system</li>

<li>Start: Salvager(big) | Argosy: equipped for boarding, in Aldhibain system</li>

<li>Start: Explorer to Remnant | Heavy Shuttle: equipped for exploring the Remnant, in Tania Australis system</li>

<li>Start: Explorer to Automata | Bounder: equipped for exploring the Kor Automata, in Mirfak system</li>

<li>Start: Cheater 1 | Heron + 10xKIV: 1b credits, full visible human space, Jump Drive, in Sol system, no story</li>

<li>Start: Cheater 2 | Heron + 10xSkylark: 1b credits, full visible human space, Jump Drive, in Sol system, no story</li>

</ul>

<br>

Beside the cheater start options, all others are balanced and lore friendly. A bigger ship means a bigger bank loan. All starts come with 200.000 credits cash and a bank loan between 600.000 and 4,5 million credits. The ships outfits are changed to fit the role. The intro missions on New Boston are set as completed. Same goes for the Hai start with the Hai first contact mission.<br>

<br>

<br>

Changelog:<br>

<br>

2024-11-02 <br>

changed cheater 2 start heron to have 20 heavy warship bays<br>

<br>

2024-10-08 <br>

proofreading and minor text changes (Vemenous-Repentile)<br>

added a new cheater start with Quarg outfits, ships and more credits<br>

<br>

2024-06-07<br>

text corrections (thx to TheGiraffe3)<br>

<br>

2024-03-15<br>

Start: Cheater, changed Heron weapons and added 10x KIV with beam weapons<br>

Start: Cheater, added mission for full visible human space to the outfitter<br>

<br>

2024-02-15<br>

Start: Cheater... fixed map not showing all systems<br>

Start: Miner... changed ship to "Sunder" with 2 Mining Drones<br>

<br>

2023-10-17<br>

added plugin.txt<br>

<br>

2023-09-15<br>

added passenger transport start<br>

set intro missions to done for all starts<br>

doubled bank loan duration / halfed interest rate for all starts<br>

changed cheater start ship and credits<br>

<br>

2023-09-03<br>

changed miner start to a system with outfitter<br>

added Start Trader Freighter<br>

added Start Trader (Hai) Aphid<br>

added Start Explorer to Remnant<br>

added Start Explorer to Automata<br>

</blockquote>
</details>
<br>
screenshots(click to enlarge):<br>
<table>
	<tr>
		<td><img src="https://raw.githubusercontent.com/zuckung/endless-sky-plugins/master/screenshots/better.starts01.jpg" width="200"></td>
	</tr>
</table>
<br>

<br>
