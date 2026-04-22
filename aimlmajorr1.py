# Advanced Plagiarism Checker

import math
import string
from collections import Counter

# ---------- Preprocessing ----------
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

# ---------- Jaccard Similarity ----------
def jaccard_similarity(words1, words2):
    set1 = set(words1)
    set2 = set(words2)

    intersection = set1 & set2
    union = set1 | set2

    score = (len(intersection) / len(union)) * 100 if union else 0
    return score, intersection

# ---------- Cosine Similarity ----------
def cosine_similarity(words1, words2):
    freq1 = Counter(words1)
    freq2 = Counter(words2)

    all_words = set(freq1.keys()) | set(freq2.keys())

    dot = sum(freq1[w] * freq2[w] for w in all_words)
    mag1 = math.sqrt(sum(v**2 for v in freq1.values()))
    mag2 = math.sqrt(sum(v**2 for v in freq2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0

    return (dot / (mag1 * mag2)) * 100

# ---------- File Reading ----------
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        print("❌ File not found!")
        return ""

# ---------- Main ----------
def main():
    print("\n📄 Advanced Plagiarism Checker")

    choice = input("\n1. Enter text manually\n2. Compare text files\nChoose option: ")

    if choice == "1":
        text1 = input("\nEnter first text:\n")
        text2 = input("\nEnter second text:\n")

    elif choice == "2":
        file1 = input("Enter first file path: ")
        file2 = input("Enter second file path: ")
        text1 = read_file(file1)
        text2 = read_file(file2)

    else:
        print("Invalid choice!")
        return

    words1 = preprocess(text1)
    words2 = preprocess(text2)

    jac_score, common = jaccard_similarity(words1, words2)
    cos_score = cosine_similarity(words1, words2)

    print("\n📊 -------- ANALYSIS REPORT --------")
    print(f"Jaccard Similarity : {jac_score:.2f}%")
    print(f"Cosine Similarity  : {cos_score:.2f}%")

    print("\n🔍 Common Words:")
    print(", ".join(list(common)[:20]) if common else "None")

    # Final interpretation
    avg_score = (jac_score + cos_score) / 2

    print("\n📌 Verdict:")
    if avg_score > 70:
        print("⚠️ High Similarity (Possible Plagiarism)")
    elif avg_score > 40:
        print("⚠️ Moderate Similarity")
    else:
        print("✅ Low Similarity (Likely Original)")

main()


#The project uses Jaccard Similarity, Cosine Similarity, tokenization, and hash-based frequency counting