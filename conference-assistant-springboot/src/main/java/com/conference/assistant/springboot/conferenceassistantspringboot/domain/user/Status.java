package com.conference.assistant.springboot.conferenceassistantspringboot.domain.user;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Status {
    INVALID("STATUS_INVALID", "탈퇴회원"),
    VALID("STATUS_VALID", "유효회원");

    private final String key;
    private final String title;
}
