{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "LIGHT_BLUE = \"C5D9F1\"\n",
    "YELLOW = \"FFFF00\"\n",
    "GRAY = \"E4DFEC\"\n",
    "DEEP_BLUE = \"1072BA\"\n",
    "DEEP_BLUE2 = \"4A9CD9\"\n",
    "WHITE = \"FFFFFF\"\n",
    "Green_Good  = \"85F386\"\n",
    "Purple_Perfect = \"E951F6\"\n",
    "Yellow_OK = \"F7F173\" \n",
    "Gray_None = \"696968\"  \n",
    "Red_Bad = \"E8241B\" \n",
    "\n",
    "Yellow_OK_Fill = PatternFill(start_color = Yellow_OK, end_color = Yellow_OK, fill_type = \"solid\")\n",
    "Purple_Perfect_Fill = PatternFill(start_color = Purple_Perfect, end_color = Purple_Perfect, fill_type = \"solid\")\n",
    "Green_Good_Fill = PatternFill(start_color = Green_Good, end_color = Green_Good, fill_type = \"solid\")\n",
    "Red_Bad_Fill = PatternFill(start_color = Red_Bad, end_color = Red_Bad, fill_type = \"solid\")\n",
    "Gray_None_Fill = PatternFill(start_color = Gray_None, end_color = Gray_None, fill_type = \"solid\")\n",
    "\n",
    "\n",
    "CONTENT_TAB_COLOR = DEEP_BLUE2\n",
    "USER_TAB_COLOR = YELLOW\n",
    "BLANK_WHITE = WHITE \n",
    "HEADER_COLOR = LIGHT_BLUE  # Light Blue - Light Blue indicates relevant content for validation \n",
    "HEADER_COLOR_USER_ENTRY = YELLOW # Yellow - Yellow indicates a field for User Entry \n",
    "HEADER_COLOR_INFORMATIONAL_ONLY = GRAY # Gray - Indicates a field that maybe helpful but for information purposes only \n",
    "Color_Scale_Rule = ColorScaleRule(start_type=\"min\",start_color=\"FF0000\",end_type=\"max\",end_color=\"99FF33\")\n",
    "Data_Bar_Rule = DataBarRule(start_type=\"min\", end_type=\"max\", color=\"00CC00\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
