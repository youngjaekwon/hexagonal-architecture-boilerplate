from app.domain.exception import error_code
from fastapi import APIRouter, Depends, status

from app.domain import schema
from app.domain.service.article.crud import ArticleCRUDService
from app.port.incoming.usecase.article.crud import ArticleCRUDUsecase

router = APIRouter()


@router.get(
    "/",
    response_model=list[schema.Article],
    response_model_exclude_none=True,
    responses={
        status.HTTP_200_OK: {
            "description": "아티클 리스트 조회 성공",
            "model": list[schema.Article],
        },
        status.HTTP_400_BAD_REQUEST: {
            "description": "아티클 리스트 조회 실패",
            "content": error_code.ArticleError.generate_error_responses_content()
        },
    }
)
async def get_articles(
        article_usecase: ArticleCRUDUsecase = Depends(ArticleCRUDService),
) -> list[schema.Article] | error_code.ArticleError:
    """
    ## 아티클 리스트 조회

    ## Error Code
    - 1000: 아티클 리스트 조회 실패
    - 1001: 아티클 리스트 조회 실패
    """
    result = await article_usecase.read_articles()
    return result


@router.post("/")
async def create_article(
        article_create: schema.ArticleCreate,
        article_usecase: ArticleCRUDUsecase = Depends(ArticleCRUDService),
) -> schema.Article:
    return await article_usecase.create_article(article_create)
