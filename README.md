# FGO-Automata

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Meowcolm024/FGO-Automata?include_prereleases)
![GitHub issues](https://img.shields.io/github/issues/Meowcolm024/FGO-Automata)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Meowcolm024/FGO-Automata)
![GitHub](https://img.shields.io/github/license/meowcolm024/FGO-Automata)

**FGO-Automata** allows you to play _Fate/GO_ just like writting *Python* Script

**注意FGO-Automata适用于国服的Fate/Grand Order.** PS：[中文版README](README_CN.md)

If you're playing with other versions of _Fate/GO_ (like TW or US), you may need to remake the template images in `/assets`

## Table of Contents

<details>

- [FGO-Automata](#fgo-automata)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Setup](#setup)
  - [⚠️ Notice](#%e2%9a%a0%ef%b8%8f-notice)
  - [References](#references)
    - [<ol>
<li>Initialization</li>
</ol>](#ol-liinitializationli-ol)
      - [<ol>
<li>Import package</li>
</ol>](#ol-liimport-packageli-ol)
      - [<ol start="2">
<li>Setup the Class</li>
</ol>](#ol-start%222%22-lisetup-the-classli-ol)
      - [<ol start="3">
<li>AP related (Optional)</li>
</ol>](#ol-start%223%22-liap-related-optionalli-ol)
    - [<ol start="2">
<li>Start battle</li>
</ol>](#ol-start%222%22-listart-battleli-ol)
    - [<ol start="3">
<li>During battle</li>
</ol>](#ol-start%223%22-liduring-battleli-ol)
      - [<ol>
<li>Select cards</li>
</ol>](#ol-liselect-cardsli-ol)
      - [<ol start="2">
<li>Select Servant skills</li>
</ol>](#ol-start%222%22-liselect-servant-skillsli-ol)
      - [<ol start="3">
<li>Select Master skills</li>
</ol>](#ol-start%223%22-liselect-master-skillsli-ol)
      - [<ol start="4">
<li>Select Servant (DEPRECATED)</li>
</ol>](#ol-start%224%22-liselect-servant-deprecatedli-ol)
      - [<ol start="5">
<li>Change Servants (DEPRECATED)</li>
</ol>](#ol-start%225%22-lichange-servants-deprecatedli-ol)
    - [<ol start="4">
<li>Finish battle</li>
</ol>](#ol-start%224%22-lifinish-battleli-ol)
    - [<ol start="5">
<li>Other functions</li>
</ol>](#ol-start%225%22-liother-functionsli-ol)
      - [<ol>
<li>Wait for a certain scene</li>
</ol>](#ol-liwait-for-a-certain-sceneli-ol)
      - [<ol start="2">
<li>Tap screen</li>
</ol>](#ol-start%222%22-litap-screenli-ol)
      - [<ol start="3">
<li>Toggle Master Skill</li>
</ol>](#ol-start%223%22-litoggle-master-skillli-ol)
  - [Making Templates](#making-templates)
  - [TO-DO](#to-do)

</details>

## Install

Required libs: *ADB*, *PIL*, *OpenCV* and *numpy*

1. Install *ADB*
   - macOS: ```brew cask install android-platform-tools```
   - Windows: ```choco install adb```
2. Install *PIL*, *OpenCV* and *numpy*: ```pip install opencv-python numpy pillow```
3. Clone the repo: ```git clone https://github.com/Meowcolm024/FGO-Automata.git```

## Setup

There are mainly 3 ways to set up *FGO-Automata*(as automation script):

- If you are familiar with _Python_, you can try to manually write the scipt. (See: [References](#references)) (You can also checkout the [example.py](example.py))
- If you are using _Windows_, double click `config.bat` to set up the script.（中文）
- If you are using _macOS_(or _Linux_), run `demon.py` to set up the script.

You can also use *FGO-Automata* as an API in your own project, just import the package :)

## ⚠️ Notice

When using FGO-Automata as a automation script, notice the following things:

1. Turn **OFF** skill confirmation(*Quick Cast*).
2. When using `config.bat` or `demon.py`, make sure you can pass the Checkpoint within **3 turns**.
3. Recommended: turn ON *Speed Up Death Animation* and *2x Speed*

## References

### 1. Initialization

#### 1. Import package

```python
from core.Automata import Automata
```

* First import the package

#### 2. Setup the Class

```python
shiki = Automata("assets/checkpoint.png", "assets/qp.png", (248, 0))
```

```python
ryougi = Automata("assets/checkpoint.png", "assets/qp.png")
```

* The first argument and the second one refers to the **path** of your **template** of checkpoint and **support servant**.
* And the third argument is also optional, if you screen resolution is *1920x1080*, just leave it blank or replace it with `(0,0)`.
* In the third argument, only add them if there are blues straps at the edges. For `(x, y)`, *x* refers to the shifts in x-axis shift, *y* refers to y-axis shift.

#### 3. AP related (Optional)

```python
# .set_apples(<number of the apples>, <path to the apples>)
shiki.set_apples(0, "assets/silver.png")
```

* If you are using it as a automation bot, you may encounter AP problem which need to use *Gold Apples*.
* Notice that the function recieves 2 arguments. The first item is number, representing how many apples will be consumed. The second one refers to the **path** of your **template** of the type of the apple (incl. *Quartz*).

### 2. Start battle

```python
# start
shiki.select_checkpoint("assets/checkpoint2.png") # the argument is optional
shiki.select_support("assets/qp2.png") # the argument is optional
shiki.start_battle()
```

* You can choose other checkpoints and supports if needed
* If you don't need to modify your checkpoints and supports you can use:

```python
shiki.quick_start()
```

> **About support selection**  
> It will onlt select the *support servant* in first page(the first 3 servants) if there isn't any match, it will automatically select the **first** support servant by default

### 3. During battle

#### 1. Select cards

```python
# .select_cards(<list of the desired cards(in order)>)
shiki.select_cards([7])
```

```python
ryougi.select_cards([1,2,3])
```

* Notice this function receives a *list* of maximum **3** numbers. If the list is empty or has less numbers, more cards from normal cards will be selected randomly.
* For the numbers' meaning: Number **1~5** refer to the *normal cards* from **left** to **right**. Number **6,7,8** refer to *NP cards*.
* Cards will be taped in orders

#### 2. Select Servant skills

```python
# skill w/o target
# .select_servant_skill(<id of the skill>)
shiki.select_servant_skill(4)
```

* Notice this function receives a number.
* The number can be in the range of **1~9**, each refers to the skill counted from left.

```python
# with target Servant
# select_servant_skill(<id of the skill>, <id of the target servant>)
ryougi.select_servant_skill(2, 3)
```

* You can also add the second argument for the target *Servant*(See: [*Select Servants*](#4-select-servant-deprecated)). The second argument receives a number. The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

#### 3. Select Master skills

```python
# skill w/o target
# .select_master_skill(<id of the skill>)
shiki.select_master_skill(2)
```

* Notice this function receives a number.
* The number can be in the range of **1~3**, each refers to the skill counted from left.

```python
# with target Servant
# .select_master_skill(<id of the skill>, <id of the target servant>)
ryougi.select_master_skill(1, 3)
```

* You can also add the second argument for target *Servant*(See: [*Select Servants*](#4-select-servant-deprecated)). The second argument receives a number. The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

```python
# Order Change
# .select_master_skill(<id of the skill>, <id of the first servant>, <id of the second servant>)
rin.select_master_skill(3, 1, 1)
```

* If the skill is *Order Change*, you can add the third argument(See: [*Change Servants*](#5-change-servants-deprecated)). In the second and third argument, each should be a number in the range of **1~3**. The second arg refers to the first 3 Servants and the third one refers to the last 3.

#### 4. Select Servant (DEPRECATED)

```python
# .select_servant(<id of the skill>)
shiki.select_servant(1)
```

* **NOTICE: This function has been integrated to `select_servant_skill` and `select_master_skill`, so you don't need to use it explicitly. (Besides, the reference below is still vaild.)**
* There are some skills in *FGO* have target servant, if the skill you have chosen is this kind of skill, you may need to use this function to choose the desired *Servant*.
* Notice this function receives a number.
* The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

#### 5. Change Servants (DEPRECATED)

```python
# .change_servant(<id of the first servant>, <id of the second servant>)
shiki.change_servant(1, 1)
```

* **NOTICE: This function has been integrated to `select_master_skill`, so you don't need to use it explicitly. (Besides, the reference below is still vaild.)**
* This function receives 2 numbers, each should be in the range of **1~3**.
* The first arg refers to the first 3 Servants and the second one refers to the last 3.

### 4. Finish battle

```python
# finish
shiki.finish_battle()
```

* This function allows the program tap through the ending of battle.

### 5. Other functions

#### 1. Wait for a certain scene

```python
shiki.wait("assets/checkpoint.png")
```

* It allows you idle the script till a certain scene
* It receives an argument of the *path* of the template image.

#### 2. Tap screen

```python
shiki.tap((100, 100), 0, 0)
```

* Allows to tap a certain point in the screen
* The first arg is a tuple of the coordinate `(x, y)`
* The 2nd and the 3rd args are random shifts in x and y, if you don't want have any shifts, replace with `0`

#### 3. Toggle Master Skill

```python
shiki.toggle_master_skill()
```

* You can use this function to turn on/off the _Master_ skill panel.

## Making Templates

Here are two examples of the template:

![checkpoint](assets/event.png)

* This is a template of a _checkpoint_

![support](assets/sp2.png)

* This is a template of the _support_

**Notice that your template should be distinctive.**

## TO-DO

- [ ] Advance support selection
