# 🎧 Playlist Iterator – Iterator Design Pattern in Python

This project demonstrates the **Iterator Design Pattern** through a simple music playlist system. The pattern allows sequential access to songs in a playlist without exposing the underlying data structure.

## 🧠 Design Pattern Overview

The **Iterator Pattern** provides a way to access elements of a collection sequentially without exposing the internal representation of the collection.

## 💡 Use Case: Music Playlist

A playlist contains a list of songs. Instead of exposing the list directly, we provide an iterator to go through the songs one by one using a `for` loop or `next()`.

## 🧱 Components

- **Aggregate**: `Playlist`  
  - Stores a list of `Song` objects.  
  - Implements `__iter__()` to return a `PlaylistIterator`.

- **Iterator**: `PlaylistIterator`  
  - Implements `__iter__()` and `__next__()`.  
  - Keeps track of the current position in the playlist.

- **Element**: `Song`  
  - Contains basic song info like title and artist.

## 🚀 How to Run

1. Make sure Python 3.6+ is installed.
2. Run the script:

```bash
python main.py
```
