    path('accounts/password_reset/', views.PasswordReset.as_view(), name="passwordChange"),
    path('accounts/password_reset_done/', views.PasswordResetDone.as_view(), name="password-reset-done"),
    path('accounts/password_reset_confirm/', views.PasswordResetConfirm.as_view(), name="password-reset-confirm")
