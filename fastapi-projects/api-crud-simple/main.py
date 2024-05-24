from fastapi import FastAPI, HTTPException

from typing import List
from uuid import UUID, uuid4
from enum import Enum

from models import Team

app = FastAPI()


class Tags(Enum):
    root = "root"
    teams = "teams"


teams = []


@app.get("/", tags=[Tags.root])
def read_root():
    return {"message": "CRUD app"}


@app.get("/teams/", tags=[Tags.teams], response_model=List[Team])
def read_teams():
    return teams


@app.get("/teams/{team_id}", tags=[Tags.teams], response_model=Team)
def read_team(team_id: UUID):
    for team in teams:
        if team.id == team_id:
            return team

    raise HTTPException(status_code=404, detail="Team Not Found!")


@app.post("/teams/", tags=[Tags.teams], response_model=Team)
def register_team(team: Team):
    team.id = uuid4()
    teams.append(team)
    return team


@app.put("/teams/{team_id}", tags=[Tags.teams], response_model=Team)
def update_team(team_id: UUID, team_updated: Team):
    for idx, team in enumerate(teams):
        if team.id == team_id:
            updated_team = team.copy(update=team_updated.dict(exclude_unset=True))
            teams[idx] = updated_team
            return updated_team

    raise HTTPException(status_code=404, detail="Team not found!")


@app.delete("/teams/{team_id}", tags=[Tags.teams], response_model=Team)
def delete_team(team_id: UUID):
    for idx, team in enumerate(teams):
        if team.id == team_id:
            teams.pop(idx)
            return team


"""
@app.patch("/teams/{team_id}", tags=[Tags.teams], response_model=Team)
def update_team(team_id: UUID, team_updated: Team):
    for idx, team in enumerate(teams):
        if team.id == team_id:
            stored_team_data = teams[idx]
            stored_team_model = Team(**stored_team_data)
            update_data = team_updated.model_dump(exclude_unset=True)
            updated_team = stored_team_model.model_copy(update=update_data)
            teams[idx] = jsonable_encoder(updated_team)
            return updated_team
"""
