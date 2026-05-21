import pytest
import asyncio
from fastapi.testclient import TestClient
from main import app
from unittest.mock import AsyncMock, patch

client = TestClient(app)

def test_get_balance_success():
    # Mock the WalletService.get_ballance method
    with patch('routers.wallet.WalletService') as mock_service:
        # Create an instance of the mock service
        mock_instance = mock_service.return_value
        mock_instance.get_ballance = AsyncMock(return_value=100.0)
        
        response = client.get("/api/v1/wallet/11111111-1111-1111-1111-111111111111")
        
        assert response.status_code == 200
        assert response.json() == {"balance": '100.0'}
        mock_instance.get_ballance.assert_called_once_with("11111111-1111-1111-1111-111111111111")

def test_get_balance_not_found():
    # Mock the WalletService.get_ballance method to return None
    with patch('routers.wallet.WalletService') as mock_service:
        mock_instance = mock_service.return_value
        mock_instance.get_ballance = AsyncMock(return_value=None)
        
        response = client.get("/api/v1/wallet/11111111-1111-1111-1111-111111111111")
        
        assert response.status_code == 404
        assert response.json() == {"detail": "Wallet not found"}

def test_make_operation_success():
    # Mock the WalletService.make_operation_balance method
    with patch('routers.wallet.WalletService') as mock_service:
        mock_instance = mock_service.return_value
        mock_instance.make_operation_balance = AsyncMock(return_value=150.0)
        
        response = client.post(
            "/api/v1/wallet/11111111-1111-1111-1111-111111111111/operation", 
            json={"operation_type": "DEPOSIT", "amount": 50.0}
        )
        
        assert response.status_code == 200
        assert response.json() == {"balance": '150.0'}
        mock_instance.make_operation_balance.assert_called_once_with(
            "11111111-1111-1111-1111-111111111111", "DEPOSIT", 50.0
        )

def test_make_operation_wallet_not_found():
    # Mock the WalletService.make_operation_balance method to raise ValueError with NotFoundWallet
    with patch('routers.wallet.WalletService') as mock_service:
        mock_instance = mock_service.return_value
        mock_instance.make_operation_balance = AsyncMock(side_effect=ValueError("NotFoundWallet"))
        
        response = client.post(
            "/api/v1/wallet/11111111-1111-1111-1111-111111111111/operation", 
            json={"operation_type": "DEPOSIT", "amount": 50.0}
        )
        
        assert response.status_code == 404
        assert response.json() == {"detail": "NotFoundWallet"}

def test_make_operation_invalid_data():
    # Mock the WalletService.make_operation_balance method to raise ValueError with other message
    with patch('routers.wallet.WalletService') as mock_service:
        mock_instance = mock_service.return_value
        mock_instance.make_operation_balance = AsyncMock(side_effect=ValueError("Invalid amount"))
        
        response = client.post(
            "/api/v1/wallet/11111111-1111-1111-1111-111111111111/operation", 
            json={"operation_type": "DEPOSIT", "amount": -50.0}
        )
        
        assert response.status_code == 422
        print(response.json())
        assert response.json()['detail'][0]['msg'] == "Input should be greater than 0"
