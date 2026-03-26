#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Replace the Open an Account paragraph
# Find and replace just the paragraph content
old_text_1 = '''<h3>Open an Account</h3>
                <p>Our experts begin with a thorough inspection of your property to identify the type of pests and assess the extent of the infestation. We'll find where they're hiding, how they're getting in, and what's keeping them around. </p>
                <span>1</span>'''

new_text_1 = '''<h3>Open an Account</h3>
                <p>Create an account in minutes and get ready to trade. Our simple registration process guides you through every step.</p>
                <a href="#" class="btn" style="margin-top: 15px;">
                  <span class="btn-wrap">
                    <span class="text-one">Read More</span>
                    <span class="text-two">Read More</span>
                  </span>
                </a>
                <span>1</span>'''

content = content.replace(old_text_1, new_text_1)

# Step 2: Replace the Select a Plan paragraph
old_text_2 = '''<h3>Select a Plan</h3>
                <p>Our experts begin with a thorough inspection of your property to identify the type of pests and assess the extent of the infestation. We'll find where they're hiding, how they're getting in, and what's keeping them around. </p>
                <span>2</span>'''

new_text_2 = '''<h3>Select a Plan</h3>
                <p>Select a plan of your choice and start to invest. Choose from our flexible investment packages tailored to your needs.</p>
                <a href="#pricing" class="btn" style="margin-top: 15px;">
                  <span class="btn-wrap">
                    <span class="text-one">Read More</span>
                    <span class="text-two">Read More</span>
                  </span>
                </a>
                <span>2</span>'''

content = content.replace(old_text_2, new_text_2)

# Step 3: Replace the Draw Profit paragraph
old_text_3 = '''<h3>Draw Profit</h3>
                <p>Our experts begin with a thorough inspection of your property to identify the type of pests and assess the extent of the infestation. We'll find where they're hiding, how they're getting in, and what's keeping them around. </p>
                <span>3</span>'''

new_text_3 = '''<h3>Draw Profit</h3>
                <p>Withdraw all your profits directly into your wallet. Fast and secure withdrawals anytime you need them.</p>
                <a href="#" class="btn" style="margin-top: 15px;">
                  <span class="btn-wrap">
                    <span class="text-one">Read More</span>
                    <span class="text-two">Read More</span>
                  </span>
                </a>
                <span>3</span>'''

content = content.replace(old_text_3, new_text_3)

# Write the file back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated How It Works section paragraphs")
