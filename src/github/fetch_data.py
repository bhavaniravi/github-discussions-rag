import os
from dotenv import load_dotenv

from src.github.data_model import Data, Question, Answer

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

load_dotenv()


# Select your transport with a defined url endpoint
token = os.environ["GITHUB_TOKEN"]
transport = AIOHTTPTransport(
    url="https://api.github.com/graphql", headers={"Authorization": f"Bearer {token}"}
)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)


get_repo_discussions_query_v2 = gql(
    """
    query GetRepositoryDiscussions($owner: String!, $project_name: String!) {
    repository(owner: $owner, name: $project_name) {
      discussions(first: 30) {
        totalCount
        pageInfo {
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
        }
        nodes {
          id
          title
          url
          createdAt
          author {
            login
            url
          }
          category {
            name
          }
          comments(first: 5){
            nodes {
              id
              author {
                login
                url
              }
              bodyText
            }
          }
        }
      }
    }
  }

"""
)


def fetch_discussions(owner, project_name):
    # Execute the query on the transport
    result = client.execute(
        get_repo_discussions_query_v2,
        variable_values={"owner": owner, "project_name": project_name},
    )

    questions = []
    for discussion in result["repository"]["discussions"]["nodes"]:
        answers = []
        for comment in discussion["comments"]["nodes"]:
            answers.append(Answer(id=comment["id"], ans=comment["bodyText"]))

        questions.append(
            Question(id=discussion["id"], question=discussion["title"], answers=answers)
        )

    print("got questions count=", len(questions))
    return Data(questions=questions)
