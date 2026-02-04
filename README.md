# Connectly API

A Django REST Framework API for a social media platform. Built for MO-IT152 at Malayan Colleges Laguna.

**Team:** John Paul P., Kurosh Avendaño, Kristine Paul Garcia

## Overview

Connectly lets users create profiles, write posts, and leave comments. This is the Week 3 version where we switched to Class-Based Views and added proper validation through DRF serializers.

## What We Built

Three main models: Users, Posts, and Comments. Users can make posts, and anyone can comment on posts. Everything connects through foreign keys so posts link to their authors and comments link to both posts and users.

The API validates everything automatically now. If you try to create a post without content or link to a user that doesn't exist, it returns proper error messages.

