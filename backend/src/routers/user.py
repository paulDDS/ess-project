from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from db import database as db
from bson import ObjectId
from typing import List
from service.user_service import UserService
from schemas.user import (
    UserModel,
    UserList
)

router = APIRouter()

@router.get(
  "/get_user/{user_id}",
  tags=['User'],
  response_model=UserModel,
  response_class=JSONResponse,
  summary="Get a specific user",
)
def get_user(user_id: str):
  user = UserService.get_user(user_id)
  
  return user

@router.get(
  "/get_all",
  tags=['User'],
  response_model=UserList,
  response_class=JSONResponse,
  summary="Get all users",
)
def get_all_users():
  users = UserService.get_users()
  return {"users": users}
  
@router.post(
  "/create_user",
  tags=['User'],
  status_code=201,
  response_model=UserModel,
  response_class=JSONResponse,
  summary="Create a user",
)
def create_user(user: UserModel):
  new_user = UserService.add_user(user)

  return new_user

@router.put(
  "/update_user/{user_id}",
  tags=['User'],
  response_model=UserModel,
  response_class=JSONResponse,
  summary="Edit a user",
)
def update_user(user_id: str, updated_user: UserModel):
  updated_user = UserService.edit_user(user_id, updated_user)
  
  return updated_user
  
@router.delete(
  "/delete_user/{user_id}",
  tags=['User'],
  response_class=JSONResponse,
  summary="Delete a user",
)
def delete_user(user_id: str, password: str):
  deleted_user = UserService.delete_user(user_id, password)
  return deleted_user

@router.delete(
  "/delete_all",
  tags=['User'],
  response_class=JSONResponse,
  summary="Delete all users",
)
def delete_all():
  UserService.delete_all_users()